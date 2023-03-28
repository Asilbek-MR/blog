from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.views.generic import DetailView,ListView,DeleteView,UpdateView
import bleach
from .forms import SearchForm
from django.http import Http404

def index(request):
    try:
        posts = Post.objects.filter(main_article=False).order_by('-created')
        posts_m=Post.objects.filter(main_article=True).last()
        category = Category.objects.all()
        context = {
            "posts":posts,
            "category":category,
            'posts_m':posts_m
        }
        return render(request,'index.html',context)
    except Http404:
        return render(request,'404.html',status=404)


def page_not_found(request,exception):
    return render(request,'404.html',status=404)

def about(request):
    return render(request,'about.html')

class PostDeatilView(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'post'

def contact(request):
    return render(request,'contact.html')

def provide(request):
    return render(request,'privacy-policy.html')

def terms(request):
    return render(request,'terms-conditions.html')

def post_search(request):
    search = request.GET.get('search')
    categorye = request.GET.get('category')
    if search:
        results = Post.objects.filter(title__icontains=search)
        return render(request, 'travel.html',{"results":results,"query":search})
    
    if categorye:
        categoryes = Post.objects.filter(category__content__icontains=categorye)
        return render(request, 'travel.html',{"query":categoryes,"results":categoryes})

def post_category(request,pk):
    
    results = Post.objects.filter(category__id=pk)

    return render(request,'travel.html', {"results":results,"count":results.count()})
   
    
def notfound(request):
    return render(request,'404.html')

