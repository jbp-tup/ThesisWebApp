from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import OfficerRegistrationForm  # OfficerEditProfileForm, MyPasswordChangeForm


@login_required
def officer_account_registration(request):
    if request.method == 'POST':
        form = OfficerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}')
            return redirect('MVNS-login')
    else:
        form = OfficerRegistrationForm()
    context = {
        'page_title': 'User Registration',
        'form': form
    }
    return render(request, 'officers/register.html', context)


@login_required
def officer_account_profile(request):
    context = {
        'page_title': 'User Profile'
    }
    return render(request, 'officers/profile.html', context)


@login_required
def officer_account_edit_profile(request):
    context = {
        'page_title': 'Edit User Profile'
    }
    return render(request, 'officers/edit_profile.html', context)
