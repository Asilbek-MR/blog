from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Contact
import bleach
from django.http import Http404


# def handler404(request, exception, template_name="404.html"):
#     # response = render_to_response(template_name)
#     # response.status_code = 404
#     return response

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

def custom404(request, exception=None):
    return render(request, '404.html', status=500)

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


def about(request):
    return render(request,'about.html')

def article(request,slug):
    slug = Post.objects.filter(slug=slug).first()
    category = Category.objects.all()
    return render(request,'article.html',{"post":slug,"category":category})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gmail = request.POST.get('email')
        body = request.POST.get('message')
        contact_=Contact.objects.create(name=name,gmail=gmail,comment=body)
        contact_.save()
        return redirect('/')
        
    return render(request,'contact.html')

def provide(request):
    return render(request,'privacy-policy.html')

def feedback(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request,'feedback.html',{"contacts":contacts})

def post_search(request):
    search = request.GET.get('search')
    categorye = request.GET.get('category')
    if search:
        results = Post.objects.filter(title__icontains=search)
        return render(request, 'search.html',{"results":results,"query":search})
    if categorye:
        categoryes = Post.objects.filter(category__content__icontains=categorye)
        return render(request, 'search.html',{"query":categoryes,"results":categoryes})

def post_category(request,pk):
    results = Post.objects.filter(category__id=pk)
    return render(request,'search.html', {"results":results,"count":results.count()})
   
    
def not_found(request):
    return render(request,'404.html')

