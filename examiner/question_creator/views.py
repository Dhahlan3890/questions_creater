from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

# Create your views here.

def question_creator_function(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
