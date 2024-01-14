from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

#creating views

def index(request):

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            #storing data in the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            #sending confirmation email
            message_body = f"A new Job Application was submitted. Thank you, {first_name}"
            email_message = EmailMessage("Form submission confirmation",message_body, to=[email])
            email_message.send()
            #to set where Django sends email from...configure in settings.py

            messages.success(request, "Form Submitted Successfully")
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')
