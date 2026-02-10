from django.urls import path
# from customer.views import customer_dashboard_view, password_change_view
from customer.views import CustomerDashboardView, CustomerPasswordChangeView


urlpatterns = [
    path('dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('password-change/', CustomerPasswordChangeView.as_view(),
         name='password_change'),
]
