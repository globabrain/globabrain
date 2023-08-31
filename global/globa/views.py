from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "about.html", {})

def home(request):
    return render(request, "home.html", {})

def features(request):

    return render(request, "features.html")

def journal(request):

    return render(request, "journal.html")


def secure(request):

    return render(request, "secure_journal.html")

def submission(request):

    return render(request, "submission.html")

def approval(request):

    return render(request, "approval.html")