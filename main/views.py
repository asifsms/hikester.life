from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from . models import Destination, Package, Itinerary, Gallery, Enquiry
from django.views.generic.list import ListView 
from django.conf import settings
# from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        contact = Enquiry(name=name,email=email,phone=number,message=message)
        contact.save()
        # print(contact)
        # try:
		# 	send_mail('enquiry',message,'asif1791995@gmail.com',['asif1791995@gmail.com']) 
		# except BadHeaderError: #add this
		# 	return HttpResponse('Invalid header found.') #add this

        # send_mail('Enquiry',
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     ['asifkaruvarapoyil@gmail.com'],
        #     fail_silently=False)
        
    places = Destination.objects.all()[:8]
    package = Package.objects.all()[:6]
    gallery = Gallery.objects.all()[:5]
    
    return render(request,'index.html',{'destinations' : places, 'packages' : package, 'gallery' : gallery})
    
    
        
def package(request, id):
    if request.method == 'GET':
        packages = Package.objects.get(id=id)
        itinerary = Itinerary.objects.filter(package__title = packages.title) 
        context = {'package':packages, 'itineraries':itinerary}
        return render(request, 'package.html',context)
def destinations(request):
    places = Destination.objects.all()
    return render(request, 'destinations.html',{'destinations' : places})

class Packages(ListView):
    model = Package
    context_object_name = 'packages'
    template_name='Packages.html'
    
def packages(request, id):
    packages = Package.objects.filter(place_id=id)
    context = {'packages':packages}
    return render(request, 'packages.html',context)

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html',{'gallerys' : gallery})

# def send_message(request):
#     if request.method== 'POST':
#         return render(request, 'index.html')