from django.shortcuts import render

#creating views

def index(request):
    return render(request, "index.html")
