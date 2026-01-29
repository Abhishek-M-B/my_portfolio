from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact 
# from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')


# @login_required(login_url='')
def contact(request):
    # 1. Handle the Form Submission (POST)
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        number = request.POST.get('phone', '').strip()
        content = request.POST.get('message', '').strip()

        # Validation
        if not (10 <= len(number) <= 12):
            messages.error(request, 'Invalid number. Please enter 10-12 digits.')
            return render(request, 'home.html')

        # Save to database
        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()
        
        messages.success(request, 'Thank You for contacting me!! Your message has been saved.')
        return redirect('home') 

    # 2. Handle the Page Load (GET)
    # This is what was missing! You must return the page for GET requests.
    return render(request, 'home.html')