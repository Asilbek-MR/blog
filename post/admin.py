from django.contrib import admin
from .models import Post, Category,Contact

class Postadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display= ('title','category','created','updated','extra_like','dis_extra_like','main_article','global_news')
    search_fields = ('title','content')

class Contactadmin(admin.ModelAdmin):
    list_display= ('name','gmail','created_at')



admin.site.register(Contact,Contactadmin)
admin.site.register(Post,Postadmin)
admin.site.register(Category)






