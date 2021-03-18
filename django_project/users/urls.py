from django.urls import path
from . import views
from .views import UserRegisterView, UserEditView, PasswordChange, ProfileCreateView, profile

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # path('profile/<slug:slug>', profile.as_view(), name='profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('profile_edit/<slug:slug>/',
    #      ProfileEditView.as_view(), name='profile-edit'),
    path('profile_edit/', views.edit_profile, name='profile-edit'),
    path('user_edit/', UserEditView.as_view(), name='user-edit'),
    path('password/', PasswordChange.as_view(), name='password-change'),
    path('create_profile/', ProfileCreateView.as_view(), name='profile-create'),
]

#path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
