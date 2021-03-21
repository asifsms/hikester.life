from django.db import models

# Create your models here.
class Destination(models.Model):
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
   
    def __str__(self):
        return self.place

class Package(models.Model):
    place = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    days = models.IntegerField()
    nights = models.IntegerField()
    price = models.IntegerField()
    about = models.TextField()
    
   
    
    def __str__(self):
        return self.title



class Itinerary(models.Model):
    days = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
    )
    package = models.ForeignKey(Package, related_name='itinerary', on_delete=models.CASCADE)
    day = models.IntegerField(choices = days, default = 1)
    schedule = models.TextField()
    
    def __str__(self):
        return '%s, %s' %(self.package.title, self.day)
        
        
class Gallery(models.Model):
    caption = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.caption
    
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()
        
    def __str__(self):
        return '%s, %s' %(self.name, self.phone)