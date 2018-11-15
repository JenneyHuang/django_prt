from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from blog.models import BlogPost
from blog.models import Employee
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.models import BlogPostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
@csrf_protect
def archive(request):
    # post = BlogPost(title='mocktitle', body = 'mockbody',
    #                 timestamp = datetime.now())
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts':posts, 'form':BlogPostForm}, RequestContext(request))

def table(request):
    names = Employee.objects.all()
    return render_to_response('blog/templates/table.html', {'names':names})

def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.timestamp = datetime.now()
            form.save()
    return HttpResponseRedirect('/blog/')

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit = False)
        post.author = request.user
        post.timestamp = datetime.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.timestamp = datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})