from allauth.account.forms import SignupForm
from apps.accounts.models import UserAccount
from django import forms

class CustomSignupForm(SignupForm):
    email = forms.EmailField(max_length=255, label="Email")
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    profile_image = forms.ImageField(required=False, label="Profile Image")
    company = forms.CharField(
        required=False,label="Company Name",max_length=255
    )
    phone = forms.CharField(max_length=20, required=False, label="Phone Number")
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.company = self.cleaned_data['company']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'client_code', 'profile_image', 'phone', 'location', 'dob', 'company','branch']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['dob'].input_formats = ['%Y-%m-%d']
