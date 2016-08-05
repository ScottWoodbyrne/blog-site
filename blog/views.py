from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import BlogPostForm
from django.shortcuts import redirect



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, "blogposts.html", {'posts': posts})


def post_list_top(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')
    posts = posts[0:5]
    return render(request, "blogposts.html", {'posts': posts})

def post_list_shortest(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = sorted(posts, key=lambda post: len(post.content))
    posts = posts[0:5]
    return render(request, "blogposts.html", {'posts': posts})

def post_list_newest(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = posts[0:5]
    return render(request, "blogposts.html", {'posts': posts})

def post_list_oldest(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').reverse()
    posts = posts[0:5]
    return render(request, "blogposts.html", {'posts': posts})

def search(request):
    searchTerm = request.POST["searchy"]
    posts = Post.objects.filter(content__icontains= searchTerm, published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, "blogposts.html", {'posts': posts})

def gettags(request, searchtag):
    posts = Post.objects.filter(tag__icontains=searchtag, published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, "blogposts.html", {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def new_post(request):
    if request.method =='POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()

    return render(request, 'blogpostform.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method =="POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date= timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form=BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form':form})

