from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def main_page(request):
    context = {"title": "Главная страница"}
    return   render(request, template_name='advertisement/main_page.html', context=context)

def about(request):
    posts = Post.objects.all().order_by('-created_at')
    per_page = 3
    paginator = Paginator(posts,per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"title": "Объявления","page_obj": page_obj}
    return   render(request, template_name='advertisement/about.html', context=context)

def settings(request):
    context = {"title": "Настройки"}
    return   render(request, template_name='advertisement/settings.html', context=context)

def support(request):
    context = {"title": "Поддержка"}
    return   render(request, template_name='advertisement/support.html', context=context)

def about_a_site(request):
    count_posts = Post.objects.count()
    context = {"title": "О Сайте","count_posts": count_posts}
    return   render(request, template_name='advertisement/about_a_site.html', context=context)

def about_a_site_about(request):
    count_posts_t = Post.objects.count()
    context = {"title": "Кол-во Объявлений","count_posts": count_posts_t}
    return   render(request, template_name='advertisement/about.html', context=context)

@login_required
def add_post(request):
    if request.method == "GET":
        post_form = PostForm(author=request.user)
        context = {"title": "Добавить пост",'form':post_form}
        return render(request,template_name='advertisement/add_post.html', context=context)

    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES, author=request.user)
        if post_form.is_valid():
            post_form.save()
    return about(request)

def read_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"title": "Информация о посте","post": post}
    return render(request, template_name='advertisement/detail_post.html', context=context)

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.author = post_form.cleaned_data['author']
            post.image = post_form.cleaned_data['image']
            post.save()
        return redirect('advertisement:read_post', slug=post.slug)
    else:
        post_form = PostForm(initial={
            "title": post.title,
            "author": post.author,
            "text": post.text,
            "image": post.image,
        })
        return render(request, template_name="advertisement/edit_post.html", context={"form":post_form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    contex = {"post": post}
    if request.method == "POST":
        post.delete()
        return redirect('advertisement:about')
    return render(request, template_name="advertisement/delete_post.html", context=contex)

def page_not_found(request, exception):
    return render(request, template_name="advertisement/404.html", context={"title": "404"})

def forbidden(request,exception):
    return render(request, template_name="advertisement/403.html", context={"title": "403"})

def server_error(request):
    return render(request, template_name="advertisement/500.html", context={"title": "500"})