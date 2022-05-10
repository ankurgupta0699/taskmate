from django.contrib import messages
from django.shortcuts import render, redirect

from accounts import forms as accounts_forms

def register(request):
    if request.method=='POST':
        register_form = accounts_forms.CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'New User Account Created')
            return redirect('register')
    else:
        register_form = accounts_forms.CustomUserCreationForm()
    
    context = {
        'register_form': register_form,
    }
    return render(request, 'register.html', context)
