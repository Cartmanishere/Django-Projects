from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Post, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages


def index(request):
    template = loader.get_template('blog/redirect.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def submitinfo(request):
    if request.method == 'POST':
        co = Contact()
        co.name = request.POST['name']
        co.message = request.POST['message']
        co.email = request.POST['mail']
        co.save()
        messages.add_message(request, messages.INFO, 'Please enter the correct username and password.')
        return render(request, 'blog/done.html', {})
    else:
        messages.add_message(request, messages.INFO, 'Please enter the correct username and password.')
        return redirect('/')