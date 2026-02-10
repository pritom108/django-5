from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

error_403_html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Denied</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">

    <div class="bg-white shadow-xl rounded-xl p-10 max-w-md text-center">
        
        <div class="text-red-500">
            <svg xmlns="http://www.w3.org/2000/svg" 
                 fill="none" viewBox="0 0 24 24" 
                 stroke-width="1.5" stroke="currentColor"
                 class="w-20 h-20 mx-auto mb-4">
                <path stroke-linecap="round" stroke-linejoin="round" 
                      d="M12 9v3m0 4h.01M5.26 5.26l13.48 13.48M3 12a9 9 0 1115.28 6.36L3.64 3.64A8.966 8.966 0 003 12z"/>
            </svg>
        </div>

        <h1 class="text-3xl font-bold text-gray-800 mb-3">
            Access Denied
        </h1>

        <p class="text-gray-600 mb-6">
            You do not have permission to access this page.
        </p>

        <a href="/" 
           class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
            Go Home
        </a>
    </div>

</body>
</html>


"""


class IsCustomerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_customer') and self.request.user.is_customer

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden(error_403_html)
        return redirect('login')


class IsSellerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_seller') and self.request.user.is_seller

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden(error_403_html)
        return redirect('login')
