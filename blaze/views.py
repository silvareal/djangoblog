from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    context_dic ={
        'boldmessage': "I am context"
    }
    render_to_response('blaze/index.html', context_dic ,context)
    return HttpResponse("<a href='blaze/about/'>about</a>")


def about(request):
    return HttpResponse("<a href='/blaze/'>index</a>")