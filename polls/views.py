from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    myName = "Neo"
    property = ["phone","laptop","home"]
    context={"name":myName,"property":property}
    return render(request, "polls/index.html", context)

# def aboutPage(request):
#     return HttpResponse('<h1>This is about page</h1>')