from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse

class Category(models.Model):
    CATEGORY_CHOICES=(('healthy','HEALTHY'),('image','photo'),('programming','PROGRAMMING'),('productive','PRODUCTIVE'),('desigin','DESIGIN'),('self_improvement','Self_Improvement'))
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


    def __str__(self):
        return self.title
    
    @property
    def post_count(self):
        posts = self.category
        return posts.count()


    

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='image/')
    content = RichTextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    extra_like = models.IntegerField(default=0)
    dis_extra_like = models.IntegerField(default=0)
    main_article = models.BooleanField()
    global_news = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    gmail = models.EmailField(blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






















