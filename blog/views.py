from django.shortcuts import render, get_object_or_404
from .models import Blogdata


def bloghome(request):
    blogdata = Blogdata.objects.order_by('-post_date')
    return render(request, 'blog/bloghome.html', {'blogdata': blogdata})


def blogmain(request, blog_id):
    blog_data = get_object_or_404(Blogdata, pk=blog_id)
    return render(request, 'blog/blogmain.html', {'blog': blog_data})
