from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == "POST":
        return render(request, "accountapp/Base_content.html",
                      context={"text": "Post nanora!"})
    else:
        return render(request, "accountapp/Base_content.html",
                      context={"text": "Cute is Justice!"})
