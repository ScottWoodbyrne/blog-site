from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import BlogPostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain

# paginator is called by all blog views to paginate the list of blog posts returned
def paginator(request, posts_list, num_per_page):
    paginator = Paginator(posts_list, num_per_page)  # Show 5 contacts per page

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return posts



def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = paginator(request,post_list, 5)
    return render(request, "blogposts.html", {'posts': posts})

def post_list_top(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')
    post_list = post_list[0:10]
    posts = paginator(request, post_list, 5)
    return render(request, "blogposts.html", {'posts': posts})

def post_list_shortest(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    post_list = sorted(post_list, key=lambda post: len(post.content))
    post_list = post_list[0:5]
    posts = paginator(request, post_list, 5)
    return render(request, "blogposts.html", {'posts': posts})

def post_list_newest(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    post_list = post_list[0:5]
    posts = paginator(request, post_list, 5)
    return render(request, "blogposts.html", {'posts': posts})

def post_list_oldest(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').reverse()
    post_list = post_list[0:5]
    posts = paginator(request, post_list, 5)
    return render(request, "blogposts.html", {'posts': posts})

def search(request):
    searchTerm = request.POST["searchy"]

    content_list = Post.objects.filter(content__icontains= searchTerm , published_date__lte=timezone.now()).order_by('-published_date')
    tag_list = Post.objects.filter(tag__icontains= searchTerm, published_date__lte=timezone.now()).order_by('-published_date')
    title_list = Post.objects.filter(title__icontains=searchTerm, published_date__lte=timezone.now()).order_by('-published_date')
    subtitle_list = Post.objects.filter(subtitle__icontains=searchTerm, published_date__lte=timezone.now()).order_by('-published_date')

    # add the four filers above together and remove duplicates
    post_list = list(chain(content_list, tag_list, title_list, subtitle_list))
    post_list = list(set(post_list))

    posts = paginator(request, post_list, 300)
    return render(request, "blogposts.html", {'posts': posts})

def gettags(request, searchtag):
    post_list = Post.objects.filter(tag__icontains=searchtag, published_date__lte=timezone.now()).order_by('-published_date')
    posts = paginator(request, post_list, 5)
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

