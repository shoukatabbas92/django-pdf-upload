from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="pdfs/login.html"), name='login'),
    path('logout/me/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('delete/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),
    path('view/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
]
