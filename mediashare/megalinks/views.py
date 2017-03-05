from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Link
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import requests
import re
import json

def check(link):
	link_match = re.search(r'/#!(.*)!(.*)$', link) or re.search(r'/#F!(.*)!(.*)$', link)
	if link_match == None:
		return False
	else:
		mega_data = [{"a":"g", "g":1, "ssl":0, "p":link_match.group(1)}]
		mega_response = requests.post("https://g.api.mega.co.nz/cs", data=json.dumps(mega_data))
		if json.loads(mega_response.text)[0] == -9:
			return False
		else:
			return True



def newindex(request):
    return render(request, 'megalinks/newindex.html', {})


def index(request, tagfilter):
    links_list = Link.objects.filter(tag=tagfilter).order_by('-date')
    user = request.user
    template = loader.get_template('megalinks/index.html')
    paginator = Paginator(links_list, 20)

    page = request.GET.get('page')
    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)
    no_of_pages = paginator.num_pages+1
    page_range = range(1,no_of_pages)
    context = {
        'links': links,
        'user': user,
        'page_range': page_range,
        'tagfilter': tagfilter,
    }
    return HttpResponse(template.render(context, request))


@login_required
def detail(request, id):
    if request.user.is_authenticated():
        try:
            link = Link.objects.get(id=id)
        except Link.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'megalinks/detail.html', {'link': link})
    else:
        return HttpResponse("You have not logged in")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            return HttpResponse("Sorry but your account is disabled")
    else:
        messages.add_message(request, messages.INFO, 'You have successfully logged in.')
        return redirect('megalinks.views.login')



def logout(request):
    logout(request)
    return redirect('megalinks.views.login')

def search(request):
    query = request.GET['query']
    links_list = Link.objects.filter(Q(title__icontains=query) | Q(tag__icontains=query)).order_by('-date')
    user = request.user
    template = loader.get_template('megalinks/search.html')
    paginator = Paginator(links_list, 20)

    page = request.GET.get('page')
    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)
    no_of_pages = paginator.num_pages+1
    page_range = range(1,no_of_pages)
    context = {
        'links': links,
        'user': user,
        'page_range': page_range,
    }
    return HttpResponse(template.render(context, request))


def requests(request):
    return render(request, 'megalinks/requests.html', {})


def activity(request):
    links_list = Link.objects.all().order_by('-date')
    user = request.user
    template = loader.get_template('megalinks/activity_feed.html')
    paginator = Paginator(links_list, 20)

    page = request.GET.get('page')
    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)
    no_of_pages = paginator.num_pages+1
    page_range = range(1,no_of_pages)
    context = {
        'links': links,
        'user': user,
        'page_range': page_range,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        passw = request.POST['password']
        if user is "":
            return HttpResponse("Enter Username")
        else:
            if passw is "":
                return HttpResponse("Enter Password")
            else:
                user = User.objects.create_user(username=user, password=passw)
                user.is_staff=True
                user.save()
                g = Group.objects.get(name='Uploaders')
                g.user_set.add(user)
                return HttpResponse("Successfully registered.")

    return render(request, 'megalinks/signup.html', {})














