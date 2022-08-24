from django.urls import path
from .views import SignUpView, UserLoginView, UserPasswordReset, UserContactView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('register/',SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="accounts:login"), name='logout'),
    path('contact_us/', UserContactView.as_view(), name='contactus'),
    path('password_reset', UserPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name= 'password_reset_complete'),
    
]