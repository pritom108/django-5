from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def seller_dashboard_view(request):
    return render(request, 'seller/dashboard.html')
