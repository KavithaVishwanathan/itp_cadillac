from django.shortcuts import render, render_to_response, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from .models import AuthUser, Cardetails, Chapters, Cardetailsupdate, Historicalinformation, HistoricalImages
from .forms import RegistrationForm, ContactForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            #login(request, user)
            return redirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
 
    return render_to_response('EB/register.html',variables,)

def success(request):
    return render_to_response('EB/success.html',)

def logout_page(request):
    logout(request)
    return redirect('/')
    #return render_to_response('EB/homepage.html',context_instance=RequestContext(request))

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            from_email = form.cleaned_data['from_email']
            content = form.cleaned_data['content']
            try:
                send_mail(contact_name, content, from_email, ['kv668@nyu.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "EB/contact.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message')
    # form_class = ContactForm

    # if request.method == 'POST':
    #     form = form_class(data=request.POST)

    #     if form.is_valid():
    #         contact_name = request.POST.get('contact_name', '')
    #         contact_email = request.POST.get('contact_email', '')
    #         form_content = request.POST.get('content', '')

    #         # Email the profile with the contact information
    #         template = get_template('EB/contact_template.txt')
    #         context = Context({
    #             'contact_name': contact_name,
    #             'contact_email': contact_email,
    #             'form_content': form_content,
    #         })
    #         content = template.render(context)

    #         email = EmailMessage(
    #             "New contact form submission",
    #             content,
    #             "Your website" +'<cadillacdatabase.org>',
    #             ['kv668@nyu.edu'],
    #             headers = {'Reply-To': contact_email }
    #         )
    #         email.send()
    #         return redirect('contact')
    
    # return render(request, 'EB/contact.html', {
    #     'form': form_class,
    # })


def home(request):
    chapters = Chapters.objects.filter(superchapterid = 1)
    chapterheading = Chapters.objects.get(pk = 1)

    return render_to_response('EB/homepage.html', {'chapters':chapters, 'chapterheading':chapterheading, 'user': request.user});

def survivors(requests):
    chapters = Chapters.objects.filter(superchapterid = 4)
    chapterheading = Chapters.objects.get(pk = 4)

    return render_to_response('EB/chapter_template.html', {'chapters':chapters, 'chapterheading':chapterheading, 'user': requests.user});

def historical(requests):
    chapters = Chapters.objects.filter(superchapterid = 3)
    chapterheading = Chapters.objects.get(pk = 3)

    return render_to_response('EB/chapter_template.html', {'chapters':chapters, 'chapterheading':chapterheading, 'user': requests.user});

def ebparts(requests):
    chapters = Chapters.objects.filter(superchapterid = 10).order_by('chaptername')
    chapterheading = Chapters.objects.get(pk = 10)
    superchapheading = chapterheading.superchapterid.chaptername
    return render_to_response('EB/chap_no_image.html', {'chapters':chapters, 'chapterheading':chapterheading, 'user': requests.user});

def ebyear(requests):
    chapters = Chapters.objects.filter(superchapterid = 46).order_by('chapterid')
    chapterheading = Chapters.objects.get(pk = 46)
    return render_to_response('EB/chapter_template.html', {'chapters':chapters, 'chapterheading':chapterheading, 'user': requests.user});
	

def CarPage(request,carnum):		
	car = Cardetails.objects.get(carnum = carnum)
	return render_to_response('cars/carpage.html',{'car':car});
	#return render_to_response('cars/carpage.html',{'cars':cars});

def historicaltemplate(request, sectionorder):
    chapterheading = Chapters.objects.get(pk = 36)
    totsectionnum = Historicalinformation.objects.all().count()   
    section = Historicalinformation.objects.get(sectionorder = sectionorder)
    section_fk = section.sectionid
    sectionimages = HistoricalImages.objects.filter(sectionid = section_fk)

    return render_to_response('EB/historicaltemplate.html', {'section': section, 'chapterheading':chapterheading, 'sectionimages':sectionimages, 'totsectionnum':totsectionnum, 'user': request.user});

def cardisplay(request,year):
    cars_list = Cardetails.objects.filter(caryear=year).order_by('carnum')
    endindex = Cardetails.objects.count()
    chapid = 'Year '+ str(year)
    chapterheading = Chapters.objects.get(chaptername = chapid)


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

    return render_to_response('EB/car_template.html', { 'cars' : cars, 'chapterheading':chapterheading, 'endindex' : endindex, 'minpage':minpage, 'maxpage':maxpage, 'updateboolean':updateboolean, 'user': request.user}, context_instance=RequestContext(request));

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

    return render_to_response('EB/carupdate_template.html', { 'updates' : updates, 'endindex' : endindex, 'minpage':minpage, 'maxpage':maxpage, 'user': request.user}, context_instance=RequestContext(request));

