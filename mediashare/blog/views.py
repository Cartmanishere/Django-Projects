from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages


def index(request):
    template = loader.get_template('blog/redirect.html')
    context = {
    }
    return HttpResponse(template.render(context, request))