# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login


def home(request):
    # if not request.user.is_authenticated:
    # # Return a login form to login
    # else:
    # return redirect('success:page')
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, 'accounts/login.html')

def logindata(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if request.user.is_authenticated:
                    return redirect('accounts:home')


    return render(request, 'accounts/login.html', {'error':'Login Failure'})
