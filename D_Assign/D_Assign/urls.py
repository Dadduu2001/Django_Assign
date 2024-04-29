from Artist import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_users
from Artist.api import urls as u



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', auth_users.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_users.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', views.home, name='home'),
    path('api/', include(u)),
    path('get_token/', views.get_token, name='get_token'),
]

