from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def index(request):
    """Returns the main dashboard for logged in users."""
    return HttpResponse('Index!')


def visualize(request):
    return HttpResponse('A cool visulization!')


@login_required
def dashboard(request):
    return HttpResponse('User profile dashboard')
