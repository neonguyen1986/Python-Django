from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    myName = "Neo"
    property = ["phone","laptop","home"]
    context={"name":myName,"property":property}
    return render(request, "polls/index.html", context)

# def aboutPage(request):
#     return HttpResponse('<h1>This is about page</h1>')

def viewlist(request):
    list_question = Question.objects.all()
    context = {'listQuestion':list_question}
    return render(request, 'polls/question_list.html', context)

# def viewlist(request):
#     list_question = get_object_or_404(Question, pk=2) # question_text="what color do you like")
#     context = {'listQuestion':list_question}
#     return render(request, 'polls/question_list.html', context)