from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import CommentForm
from .models import Blog, Comment

def all_blogs(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list':blog_list
    }
    return render(request, 'all_blogs.html', context)

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.blog = blog
            form.save()
            return redirect(reverse('blog:blog_detail', kwargs={
                'id': blog.id
            }))
    context = {
        'blog': blog,
        'form': form,
    }


    return render(request, 'blog_detail.html', context)


def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('/')