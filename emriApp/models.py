from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200, null=True, blank=True)
    category_image= models.ImageField(upload_to='item/', null=True, blank=True)
    category_slug=models.SlugField(unique=True, null=True, blank=True)



class Item(models.Model):
    item_name= models.CharField(max_length=200, null=True, blank=True)
    item_decription= models.TextField(max_length=1000, null=True, blank=True)
    item_motorri=models.FloatField(null=True, blank=True)
    item_lloji=models.CharField(max_length=200, null=True, blank=True)
    item_karburanti=models.CharField(max_length=200, null=True, blank=True)
    item_vitiprodhimit=models.IntegerField(null=True, blank=True)
    item_image = models.ImageField(upload_to='item/', null=True, blank=True)
    item_category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.item_name}"

class Contact(models.Model):
    contact_name= models.CharField(max_length=200, null=True, blank=True)
    contact_surname= models.CharField(max_length=200, null=True, blank=True)
    contact_email=models.EmailField(max_length=200, null=True, blank=True)
    contact_description=models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"