from django import forms
from django.forms import formset_factory
from apps.core.models import FCYExchangeRequestMaster, FCYDenoMasterTable, CurrencyTable

class FCYExchangeRateUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')



class FCYExchangeRequestMasterForm(forms.ModelForm):
    class Meta:
        model = FCYExchangeRequestMaster
        fields = ['preferredBranch', 'totalEquivalentNPR', 'totalEquivalentNPRToWords']

    totalEquivalentNPR = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    preferredBranch = forms.CharField(max_length=50,required=True)
    totalEquivalentNPRToWords = forms.CharField(max_length=300,required=True)


class FCYDenoMasterTableForm(forms.ModelForm):
    currency = forms.ModelChoiceField(queryset=CurrencyTable.objects.all(), to_field_name='cyc_desc', required=True)
    
    class Meta:
        model = FCYDenoMasterTable
        fields = ['currency', 'unit', 'rate', 'deno', 'equivalentNPR']
    
    def __init__(self, *args, **kwargs):
        super(FCYDenoMasterTableForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = True
            field.widget.attrs['class'] = 'form-control'
            
            if field_name == 'equivalentNPR':
                field.widget.attrs['readonly'] = True

            if field_name == 'rate':
                field.widget.attrs['readonly'] = True

        self.currency_denominations = {
            'USD': [1, 2, 5, 10, 20, 50, 100],
            'EUR': [20, 5, 10, 50, 100, 200],
            'GBP': [20, 5, 10,50],
            'AUD': [1,2,100,20, 5, 10,50],
            'CHF': [100,20, 10,50,200],
            'CAD':[5,10,20,50,100],
            'SGD':[2,5,10,20,25,50,100,200],
            'CNY':[1,2,5,10,20,50,100],
            'SAR':[1,5,10,20,50,100,200,500],
            'QAR':[1,5,10,50,100,500],
            'THB':[20,50,100,500],
            'AED':[5,10,20,50,100,200,500],
            'MYR':[1,5,10,20,50,100],
            'SEK':[20,50,100,200,500],
            'DKK':[10,20,50,100,200],
            'HKD':[10,20,50,100,500],
            'INR':[100],
            'KRW':[500,1000, 10000,50000],
            'JPY':[1000],
            'KWD':[0.25,0.5,1,5,10,20],
            'BHD':[0.5,1,5,10,20,100],  
        }
    
    def clean(self):
        cleaned_data = super().clean()
        currency = cleaned_data.get('currency')
        deno = cleaned_data.get('deno')

        if currency and currency.cyc_desc in self.currency_denominations:
            valid_denominations = self.currency_denominations[currency.cyc_desc]
            if deno not in valid_denominations:
                self.add_error('deno', forms.ValidationError(f'For {currency.cyc_desc}, Deno must be {", ".join(str(d) for d in valid_denominations)}.'))
        
        return cleaned_data

    def label_from_instance(self, obj):
        return obj.cyc_desc
    
