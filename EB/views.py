from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Cardetails
from django.template import RequestContext

def home(requests):
	cars = Cardetails.objects.all()
	return render_to_response('EB/homepage.html');

def survivors(requests):
	cars = Cardetails.objects.all()
	return render_to_response('EB/chapter_template.html');
	


# def CarPage(request,carnum):		
# 	car = Cardetails.objects.get(carnum = carnum)
# 	return render_to_response('cars/carpage.html',{'car':car});
	#return render_to_response('cars/carpage.html',{'cars':cars});

def cardisplay(request):
    cars_list = Cardetails.objects.all().order_by('carnum')
    endindex = Cardetails.objects.count()

    paginator = Paginator(cars_list, 1)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        cars = paginator.page(page)
    except(EmptyPage, InvalidPage):
        cars = paginator.page(paginator.num_pages)
    
    if cars.number < 6:
    	minpage = 1
    	maxpage = (6 - cars.number) + 6 + cars.number
    elif cars.number > (endindex - 6):
    	minpage = cars.number - ((6 - (endindex - cars.number)) + 6)
    	maxpage = endindex
    else:
	    minpage = cars.number - 6
	    maxpage = cars.number + 6

    return render_to_response('EB/car_template.html', { 'cars' : cars, 'endindex' : endindex, 'minpage':minpage, 'maxpage':maxpage}, context_instance=RequestContext(request));


