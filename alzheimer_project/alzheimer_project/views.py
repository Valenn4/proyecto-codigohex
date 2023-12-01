from django.shortcuts import render

def about(request):
    
    return render(request,"about.html")

def profile(request):
    
    return render(request,"profile.html")
    