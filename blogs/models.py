from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


#catergory model
class caterory(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    images=models.ImageField(upload_to='caterory/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['title'] 

    def images_tag(self):
        return format_html('<img src="/media/{}" style="width:30px; height:30px; border-radius:20%"/>'.format(self.images))
    
    def __str__(self):
        return self.title
       

#post model

class post(models.Model): 
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=HTMLField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(caterory,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title

