from django.shortcuts import render
from allauth.account.views import SignupView
from apps.accounts.forms import CustomSignupForm
from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from apps.accounts.models import UserAccount, UserDetails
from apps.accounts.forms import EditProfileForm
from apps.branches.models import Branches
from allauth.account.forms import ChangePasswordForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        # Call the parent class's form_valid method to perform user registration
        response = super().form_valid(form)

        # Add a success message
        messages.success(self.request, "Registration successful. You can now log in.")

        return response


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        # Retrieve the email parameter from self.kwargs
        email = self.kwargs.get('email')
        
        # Check if the email parameter matches the authenticated user's email
        if email != request.user.email:
            messages.warning(request, "You are not authorized to edit other profiles.")
            return redirect('accounts:profile', email=request.user.email)

        # Query the UserAccount using the email parameter
        userprofiledata = UserAccount.objects.get(email=email)
        branches =  Branches.objects.filter(Status = 'T',EmailStatus = 'T')
        context = {'userprofiledata': userprofiledata, 'branches': branches}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Retrieve the email parameter from self.kwargs
        email = self.kwargs.get('email')

        # Check if the email parameter matches the authenticated user's email
        if email != request.user.email:
            messages.warning(request, "You are not authorized to edit other profiles.")
            return redirect('accounts:profile', email=request.user.email)

        userprofiledata = UserAccount.objects.get(email=email)
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=userprofiledata)

        if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(request, "Profile update failed. Please check the form data.")

        return redirect('accounts:profile', email=email)


class ProfileSecurityView(View):
    
    template_name = 'account/password_change.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

class ProfileNotificationView(View):
    
    template_name = 'account/account-notifications.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
    
@csrf_exempt
def getuserprofiledata(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)

        if username:
            # Fetch user profile data based on username (MainCode)
            try:
                user_profile = UserDetails.objects.get(MainCode=username)
    
                # Prepare the data to send in the response
                data = {
                    'BranchCode': user_profile.BranchCode,
                    'BranchName': user_profile.BranchName,
                    'Name': user_profile.Name,
                    'Address': user_profile.Address,
                    'Pan': user_profile.Pan,
                    'Mobile': user_profile.Mobile,
                }

                return JsonResponse(data)
            except UserDetails.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'Username not provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid responce'})
