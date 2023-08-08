
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post.views import custom404
from post.sitemaps import PostSitemaps

sitemaps = {
    'sitemaps': PostSitemaps
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap ,{ 'sitemaps': sitemaps }),
    path('',include('post.urls')),
]
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404  = custom404