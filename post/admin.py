from django.contrib import admin
from .models import Post, Category

class Postadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display= ('title','category','created','updated','extra_like','dis_extra_like','main_article')
    search_fields = ('title','content')

admin.site.register(Post,Postadmin)
admin.site.register(Category)





