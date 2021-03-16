from django.urls import path
from . import views
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit/', UserEditView.as_view(), name='edit'),
]

#path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
