from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def features(request):

    return render(request, "features.html")

def journal(request):

    return render(request, "journal.html")