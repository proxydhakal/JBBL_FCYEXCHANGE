from django.urls import path, include
from apps.accounts.views import UserProfileView, ProfileNotificationView, ProfileSecurityView,getuserprofiledata

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:email>', UserProfileView.as_view(), name='profile'),
    path('profile/setting/', ProfileSecurityView.as_view(), name='setting'),
    path('profiledetails/', getuserprofiledata, name='profiledetails'),
    path('profile/notification/', ProfileNotificationView.as_view(), name='notification'),
]