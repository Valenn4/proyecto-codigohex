from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Activity
# Create your views here.

@login_required(redirect_field_name=None, login_url='login')
def calender(request):
    context = {
        "activities": Activity.objects.filter(user=request.user)
    }
    return render(request,'calender/calender.html', context)
