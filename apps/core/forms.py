from django import forms
from django.forms import formset_factory
from apps.core.models import FCYExchangeRequestMaster, FCYDenoMasterTable, CurrencyTable
from apps.branches.models import Branches

class FCYExchangeRateUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')



class FCYExchangeRequestMasterForm(forms.ModelForm):
    preferredBranch = forms.ModelChoiceField(
        queryset=Branches.objects.filter(Status='T'),
        to_field_name='BranchCode',
        required=True,
        empty_label='Select Branch',
        widget=forms.Select(attrs={'class': 'SelectBranch'}),
    )

    class Meta:
        model = FCYExchangeRequestMaster
        fields = ['preferredBranch', 'totalEquivalentNPR', 'totalEquivalentNPRToWords']
        
    def __init__(self, *args, **kwargs):
        super(FCYExchangeRequestMasterForm, self).__init__(*args, **kwargs)
        
        self.fields['preferredBranch'].choices = self.get_branch_choices()
        
        for field_name, field in self.fields.items():
            field.required = True
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'


    def get_branch_choices(self):
        choices = [(branch.BranchCode, branch.BranchName) for branch in Branches.objects.all()]
        return [('', self.fields['preferredBranch'].empty_label)] + choices


class FCYDenoMasterTableForm(forms.ModelForm):
    currency = forms.ModelChoiceField(queryset=CurrencyTable.objects.exclude(cyc_desc='NPR'), to_field_name='cyc_desc', required=True)
    
    class Meta:
        model = FCYDenoMasterTable
        fields = ['currency', 'unit', 'rate', 'deno', 'equivalentNPR']
    
    def __init__(self, *args, **kwargs):
        super(FCYDenoMasterTableForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            self.fields['currency'].empty_label = 'Select Currency'
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
    
class DenoApprovedForm(forms.ModelForm):
    ACTION_TYPES = (
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    )
    
    remarks = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter remarks'}), required=True)
    action = forms.ChoiceField(choices=ACTION_TYPES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    depositedby = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Please Enter Depositor's Name"}), required=True)

    class Meta:
        model = FCYExchangeRequestMaster  
        fields = ['remarks', 'action', 'depositedby']
        
    def __init__(self, *args, **kwargs):
        super(DenoApprovedForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if field_name == 'action':
                field.empty_label = 'Select Action'
    
