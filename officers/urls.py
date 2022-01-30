from django.urls import path, reverse_lazy
from . import views
from .forms import MyPasswordChangeForm, MyLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.officer_account_registration, name='officer-register'),
    path('login/', auth_views.LoginView.as_view(template_name='officers/login.html',
                                                authentication_form=MyLoginForm,), name='MVNS-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='officers/logout.html'), name='MVNS-logout'),
    path('profile/', views.officer_account_profile, name='officer-profile',),
    # path('edit_profile/', views.officer_account_edit_profile, name='officer-edit-profile'),
    path('change_password/',
         auth_views.PasswordChangeView.as_view(template_name='officers/change_password.html',
                                               success_url=reverse_lazy('officer-change-password-done'),
                                               form_class=MyPasswordChangeForm),
         name='officer-change-password',),
    path('password_change_success/',
         auth_views.PasswordChangeDoneView.as_view(template_name='officers/password_change_done.html'),
         name='officer-change-password-done'),
]
