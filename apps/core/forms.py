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
    currency = forms.ModelChoiceField(queryset=CurrencyTable.objects.all().order_by('cyc_code'), to_field_name='cyc_desc', required=True)
    
    class Meta:
        model = FCYDenoMasterTable
        fields = ['currency', 'unit', 'rate', 'deno', 'equivalentNPR']
    
    def __init__(self, *args, **kwargs):
        super(FCYDenoMasterTableForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = True

            # Add Bootstrap classes to form fields
            if field_name == 'currency':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

            if field_name == 'equivalentNPR':
                field.widget.attrs['readonly'] = True
    
    def clean(self):
        cleaned_data = super().clean()
        currency = cleaned_data.get('currency')
        deno = cleaned_data.get('deno')

        if currency and currency.cyc_desc == 'USD':
            if deno not in [1,2 ,5, 10,20,50,100]:
                self.add_error('deno', forms.ValidationError('For USD, Deno must be 1,2 ,5, 10,20,50,100.'))
                
        if currency and currency.cyc_desc == 'EUR':
            if deno not in [20, 5, 10,50,100,200]:
                self.add_error('deno', forms.ValidationError('For EUR, Deno must be 20, 5, 10,50,100,200.'))
                
        if currency and currency.cyc_desc == 'GBP':
            if deno not in [20, 5, 10,50]:
                self.add_error('deno', forms.ValidationError('For GBP, Deno must be 20, 5, 10,50.'))
                
        if currency and currency.cyc_desc == 'AUD':
            if deno not in [1,2,100,20, 5, 10,50]:
                self.add_error('deno', forms.ValidationError('For AUD, Deno must be 1,2,100,20, 5, 10,50.'))
                
        if currency and currency.cyc_desc == 'CHF':
            if deno not in [100,20, 10,50,200]:
                self.add_error('deno', forms.ValidationError('For CHF, Deno must be 100,20, 10,50,200.'))
                
        if currency and currency.cyc_desc == 'CAD':
            if deno not in [5,10,20,50,100]:
                self.add_error('deno', forms.ValidationError('For CAD, Deno must be 5,10,20,50,100.'))
                
        if currency and currency.cyc_desc == 'SGD':
            if deno not in [2,5,10,20,25,50,100,200]:
                self.add_error('deno', forms.ValidationError('For SGD, Deno must be 2,5,10,20,25,50,100,200.'))
                
        if currency and currency.cyc_desc == 'CNY':
            if deno not in [1,2,5,10,20,50,100]:
                self.add_error('deno', forms.ValidationError('For CNY, Deno must be 1,2,5,10,20,50,100.'))
                
        if currency and currency.cyc_desc == 'SAR':
            if deno not in [1,5,10,20,50,100,200,500]:
                self.add_error('deno', forms.ValidationError('For SAR, Deno must be 1,5,10,20,50,100,200,500.'))
                
        if currency and currency.cyc_desc == 'QAR':
            if deno not in [1,5,10,50,100,500]:
                self.add_error('deno', forms.ValidationError('For QAR, Deno must be 1,5,10,50,100,500.'))
                
        if currency and currency.cyc_desc == 'THB':
            if deno not in [20,50,100,500]:
                self.add_error('deno', forms.ValidationError('For THB, Deno must be 20,50,100,500.'))
                
        if currency and currency.cyc_desc == 'AED':
            if deno not in [5,10,20,50,100,200,500]:
                self.add_error('deno', forms.ValidationError('For AED, Deno must be 5,10,20,50,100,200,500.'))
                
        if currency and currency.cyc_desc == 'MYR':
            if deno not in [1,5,10,20,50,100]:
                self.add_error('deno', forms.ValidationError('For MYR, Deno must be 1,5,10,20,50,100.'))
                
        if currency and currency.cyc_desc == 'SEK':
            if deno not in [20,50,100,200,500]:
                self.add_error('deno', forms.ValidationError('For SEK, Deno must be 20,50,100,200,500.'))
                
        if currency and currency.cyc_desc == 'DKK':
            if deno not in [10,20,50,100,200]:
                self.add_error('deno', forms.ValidationError('For DKK, Deno must be 10,20,50,100,200.'))
                
        if currency and currency.cyc_desc == 'HKD':
            if deno not in [10,20,50,100,500]:
                self.add_error('deno', forms.ValidationError('For HKD, Deno must be 10,20,50,100,500.'))
                
        if currency and currency.cyc_desc == 'INR':
            if deno not in [100]:
                self.add_error('deno', forms.ValidationError('For INR, Deno must be 100.'))
                
        if currency and currency.cyc_desc == 'JPY':
            if deno not in [1000]:
                self.add_error('deno', forms.ValidationError('For JPY, Deno must 1000.'))
                
        if currency and currency.cyc_desc == 'KRW':
            if deno not in [500,50000]:
                self.add_error('deno', forms.ValidationError('For KRW, Deno must be 500,50000.'))
                
        if currency and currency.cyc_desc == 'KWD':
            if deno not in [0.25,0.5,1,5,10,20]:
                self.add_error('deno', forms.ValidationError('For KWD, Deno must be 0.25,0.5,1,5,10,20.'))
                
        if currency and currency.cyc_desc == 'BHD':
            if deno not in [0.5,1,5,10,20,100]:
                self.add_error('deno', forms.ValidationError('For BHD, Deno must be 0.5,1,5,10,20,100.'))

        return cleaned_data

    def label_from_instance(self, obj):
        return obj.cyc_desc
