from django.contrib.sitemaps import Sitemap
from post.models import Post

class PostSitemaps(Sitemap):
    priority = 9.0
    print(priority,'0000000')
    # changefreq = 'yearly'
    
    # def items(self):
    #     return ['created']
    
    # def location(self, item):
    #     return reverse(item)
    def items(self):
        return Post.objects.all()





