from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}
    return render(request, 'poll/list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'poll/detail.html', context)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
