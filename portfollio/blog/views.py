from django.shortcuts import render,get_object_or_404
from .models import blog
blog=blog.objects
# Create your views here.
def allblogs(request):
    global blog
    return render(request,'blog/blog.html',{"blog":blog})
def details(request,blog_id):
    blog_details=get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/details.html',{'details':details})
