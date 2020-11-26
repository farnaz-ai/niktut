import Blog from './models.py'

from django.shortcuts import render , get_object_or_404


# Create your views here.
def all_blogs (request):
    blogs = Blog.objecs.all()
    return render(request, 'templates/blog/all_blogs.html', {'blogs' = blogs})
def detail(request , blog_id):
    blog = get_object_or_404 (Blog , pk=blog_id)
    return render (request , 'blog/detail.html' ,{'id':blog_id} )
