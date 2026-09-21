from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, ContactMessage

def home_view(request):
    all_projects = Project.objects.all()
    return render(request, 'home.html', {'projects': all_projects})


def about_view(request):
    # Enforce POST handling because the mini-contact form lives inside about.html
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        # Trigger success notification message alert
        messages.success(request, "Your message has been sent securely from the About page!")
        return redirect('about')
        
    return render(request, 'about.html')


def services_view(request):
    return render(request, 'services.html')


def contact_view(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        # Trigger success notification message alert
        messages.success(request, "Thank you! Your message has been saved successfully.")
        return redirect('contact')
        
    return render(request, 'contact.html')
