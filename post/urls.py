from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.post_search, name='search'),
    path('category/<int:pk>/',views.post_category,name="cat"),
    path('about/',views.about, name='about'),
    path('404/',views.notfound, name='404'),
    path('article/<slug:slug>/',views.PostDeatilView.as_view(), name='article'),
    path('contact/',views.contact, name='contact'),
    path('provide/',views.provide, name='provide'),
    path('terms/',views.terms, name='terms'),
]

handler404 = views.page_not_found


