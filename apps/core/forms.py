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
    
    currency = forms.ModelChoiceField(queryset=CurrencyTable.objects.all(),to_field_name='cyc_code', required=True)
    
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
                
    def label_from_instance(self, obj):
        return obj.cyc_desc