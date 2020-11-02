from django.db import models

#for slug field
from django.utils.text import slugify

#for ckeditor rich text field
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.CharField(max_length=100)
    roles = models.CharField(max_length=200)
    picture = models.ImageField(null=True,blank=True,upload_to="images",default="placeholder.png")
    background_image = models.ImageField(null=True,blank=True,upload_to="images",default="placeholder.png")
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    contact_text = models.TextField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    pinterest = models.URLField()
    
    #to display 'About Me' text on admin area
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100,default='0')

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(null=True,blank=True,upload_to="images",default="placeholder.png")
    tag = models.CharField(max_length=50)
    created = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200,null=True,blank=True)
    body = RichTextUploadingField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True,blank=True,upload_to="images",default="placeholder.png")
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.title)
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
            
            self.slug = slug
        
        super().save(*args, **kwargs)