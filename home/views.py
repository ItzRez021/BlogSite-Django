from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Blog
from django.conf import settings
import jdatetime
from django.core.paginator import Paginator

class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request):
        blg_list = Blog.objects.all().order_by('-created') 

        paginator = Paginator(blg_list, 6) 
        page_number = request.GET.get('page') 
        page_obj = paginator.get_page(page_number)

        blogs_with_shamsi = []
        for blog in page_obj:
            shamsi_date = jdatetime.datetime.fromgregorian(datetime=blog.created).strftime("%Y / %m / %d")
            blogs_with_shamsi.append({
                'blog': blog,
                'shamsi_date': shamsi_date,
            })
        blogs = Blog.objects.all().order_by('-created')[:5]
        context = {
            'page_obj': page_obj, 
            'blogs_with_shamsi': blogs_with_shamsi,
            'MU': settings.MEDIA_URL,
            'blogs':blogs,
        }
        return render(request, self.template_name, context)

    
class ProjectsView(View):
    template_name = 'home/project.html'
    def get(self,request):
        return render(request,self.template_name,{'MU':settings.MEDIA_URL})
    
class AboutView(View):
    template_name = 'home/about.html'
    def get(self,request):
        return render(request,self.template_name,{'MU':settings.MEDIA_URL})
    
class NewsLetterView(View):
    template_name = 'home/newsletter.html'
    def get(self,request):
        blogs = []
        for blog in Blog.objects.all().order_by('-created')[:4]:
            shamsi_date = jdatetime.datetime.fromgregorian(datetime=blog.created).strftime("%Y / %m / %d")
            blogs.append({
                'blog': blog,
                'shamsi_date': shamsi_date,
            })

        return render(request,self.template_name,{'MU':settings.MEDIA_URL,'blg':blogs})
    

class BlogDetailView(View):
    template_name = 'home/detail-blog.html'
    def get(self,request,*args,**kwargs):
        blg = get_object_or_404(Blog,pk=self.kwargs['pk'])
        uploaded_at_shamsi = jdatetime.datetime.fromgregorian(
                datetime=blg.created
            ).strftime("%Y / %m / %d")
        blog = Blog.objects.all().order_by('-created')[:5]
        return render(request,self.template_name,{'blog':blog,'MU':settings.MEDIA_URL,'blg':blg,'uploaded_at_shamsi':uploaded_at_shamsi})