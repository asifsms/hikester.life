from django.contrib import admin
from . models import Package, Destination, Itinerary, Gallery, Enquiry

# Register your models here.
admin.site.register(Package)
admin.site.register(Destination)
admin.site.register(Itinerary)
admin.site.register(Gallery)
admin.site.register(Enquiry)