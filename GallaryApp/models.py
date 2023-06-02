from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    desc= models.TextField()
    cat=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)  
    image=models.ImageField(upload_to='Images/',blank=True)   
