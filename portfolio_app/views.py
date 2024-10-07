# portfolio_app/views.py
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from portfolio_app.models import Project
from .forms import ContactForm

from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            try:
                send_mail(
                    f'New contact form submission from {name}',
                    f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                    email,
                    ['shabnashereef313@gmail.com'],  # Replace with your email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
            
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()  # Use the Project model to fetch all projects
    return render(request, 'projects.html', {'projects': projects})



def about(request):
    return render(request, 'about.html')


