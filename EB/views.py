from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (login as auth_login,  authenticate)
from django.core.urlresolvers import reverse
from .models import Cardetails, Chapters, Cardetailsupdate, Historicalinformation


def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'EB/login.html', context)


def home(requests):
    chapters = Chapters.objects.filter(superchapterid = 1)
    chapterheading = Chapters.objects.get(pk = 1)

    return render_to_response('EB/homepage.html', {'chapters':chapters, 'chapterheading':chapterheading});

def survivors(requests):
    chapters = Chapters.objects.filter(superchapterid = 4)
    chapterheading = Chapters.objects.get(pk = 4)

    return render_to_response('EB/chapter_template.html', {'chapters':chapters, 'chapterheading':chapterheading});

def historical(requests):
    chapters = Chapters.objects.filter(superchapterid = 3)
    chapterheading = Chapters.objects.get(pk = 3)

    return render_to_response('EB/chapter_template.html', {'chapters':chapters, 'chapterheading':chapterheading});

def ebparts(requests):
    chapters = Chapters.objects.filter(superchapterid = 10).order_by('chapterid')
    chapterheading = Chapters.objects.get(pk = 3)
    return render_to_response('EB/chap_no_image.html', {'chapters':chapters, 'chapterheading':chapterheading});
	

def CarPage(request,carnum):		
	car = Cardetails.objects.get(carnum = carnum)
	return render_to_response('cars/carpage.html',{'car':car});
	#return render_to_response('cars/carpage.html',{'cars':cars});

def historicaltemplate(request, sectionorder):        
    section = Historicalinformation.objects.get(sectionorder = sectionorder)
    return render_to_response('historicaltemplate.html', {'section': section});

def cardisplay(request):
    cars_list = Cardetails.objects.all().order_by('carnum')
    endindex = Cardetails.objects.count()
    chapterheading = Chapters.objects.get(pk =46)


    paginator = Paginator(cars_list, 1)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    curpage = page

    viewupdate = Cardetailsupdate.objects.filter(carnum=curpage)
    
    if viewupdate.exists():
        updateboolean = True
    else:
        updateboolean = False


    try:
        cars = paginator.page(page)
    except(EmptyPage, InvalidPage):
        cars = paginator.page(paginator.num_pages)
    
    if cars.number < 5:
    	minpage = 1
    	maxpage = (5 - cars.number) + 5 + cars.number
    elif cars.number > (endindex - 5):
    	minpage = cars.number - ((5 - (endindex - cars.number)) + 5)
    	maxpage = endindex
    else:
	    minpage = cars.number - 5
	    maxpage = cars.number + 5

    return render_to_response('EB/car_template.html', { 'cars' : cars, 'chapterheading':chapterheading, 'endindex' : endindex, 'minpage':minpage, 'maxpage':maxpage, 'updateboolean':updateboolean}, context_instance=RequestContext(request));

def carupdates(request, carnum):
    update_list = Cardetailsupdate.objects.filter(carnum=carnum)
    endindex = update_list.count()

    paginator = Paginator(update_list, 1)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1


    try:
        updates = paginator.page(page)
    except(EmptyPage, InvalidPage):
        updates = paginator.page(paginator.num_pages)
    
    if updates.number < 6:
        minpage = 1
        maxpage = (6 - updates.number) + 6 + updates.number
    elif updates.number > (endindex - 6):
        minpage = updates.number - ((6 - (endindex - updates.number)) + 6)
        maxpage = endindex
    else:
        minpage = updates.number - 6
        maxpage = updates.number + 6

    return render_to_response('EB/carupdate_template.html', { 'updates' : updates, 'endindex' : endindex, 'minpage':minpage, 'maxpage':maxpage}, context_instance=RequestContext(request));


