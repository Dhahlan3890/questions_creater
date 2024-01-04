# urls.py
from django.urls import path
from .views import upload_pdf, success_page

urlpatterns = [
    path('upload/', upload_pdf, name='upload_pdf'),
    path('success_page/<str:result>/', success_page, name='success_page'),  # Update this line
    # Add other URL patterns as needed
]
