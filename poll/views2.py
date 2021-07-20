from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    #return HttpResponse("안녕하세요 설문조사 페이지입니다.")
    question_list = Question.objects.order_by('-pub_date')
    list = ', '.join([q.question_text for q in question_list])
    return HttpResponse(list)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
