from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm


class OfficerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    # middle_initial = forms.CharField(max_length=3)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        # 'middle_initial',

    def __init__(self, *args, **kwargs):
        super(OfficerRegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        for password_field in ['password1', 'password2']:
            self.fields[password_field].widget.attrs['type'] = 'password'
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        # self.fields['middle_initial'].label = 'Middle Initial'
        self.fields['last_name'].label = 'Last Name'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'

'''
class OfficerEditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ()
'''


class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs = {'class': 'form-control'}


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['old_password', 'new_password1', 'new_password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].label = 'Old Password'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'New Password Confirmation'
