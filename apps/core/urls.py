# duplicate_finder/urls.py
from django.urls import path
from apps.core import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('createfcyexchange/', views.FCYExchangeRequestCreateView.as_view(), name='createfcyexchange'),
    path('branches/', views.BranchListView.as_view(), name='branches'),
    path('fcyexchangerate/', views.FCYExchangeRateUploadView.as_view(), name='fcyexchangerate'),
    path('fcyexchangerateview/', views.FCYExchnageRateView.as_view(), name='fcyexchangerateview'),
    path('fcyexchangerequest/', views.FCYRequestView.as_view(), name='fcyexchangerequest'),
    path('detail/fcyexchangerequest/<int:id>/', views.FCYRequestDetailView.as_view(), name='fcyexchangedetail'),
    path('edit/fcyexchangerequest/<int:id>/', views.FCYRequestEditView.as_view(), name='fcyexchangeedit'),
    path('editown/fcyexchangerequest/<int:id>/', views.FCYOwnRequestEditView.as_view(), name='fcyexchangeeditown'),
    path('convert_to_words/', views.convert_to_words, name='convert_to_words'),
    path('getdenorate/', views.getdenowiserate, name='getdenorate'),
    path('getexchnagereceipt/<int:id>/', views.generate_pdf_receipt, name='getreceipt'),
    path('batchdump/<int:id>/', views.generate_xls_batch, name='batchdump'),
    path('downloadreport/', views.generate_xls_deno_report, name='denoreportdump'),
    path('update_fcy_data/<int:fcy_id>/<int:masterId>/', views.update_fcy_data, name='update_fcy_data'),
]
