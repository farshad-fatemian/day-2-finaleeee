from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, DateTimeField, HiddenInput

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    
    
    @property
    def dollar_amount(self):
        return "$%s" % self.price if self.price else ""
    
    @property
    def availability(self):
        return "%s" % "موجود" if self.available else "ناموجود"
    
    
    
    def __str__(self):
        return self.name