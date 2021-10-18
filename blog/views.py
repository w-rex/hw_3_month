import random

from django.contrib.redirects.models import Redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Blog, Comments

# Create your views here.


def hello(request):
    return HttpResponse("Hello world")


def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(number)


def blog_view(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", context={"blog": blog})


def detail_post(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        return render(request, "blog_error.html")
    if request.method == 'POST':
        text = request.POST.get("comment", None)

        if not text:
            comments = Comments.objects.create(blog_id=id)
            return render(request, 'blog_detail.html', context={'blog': blog, "comments": comments})
        else:
            Comments.objects.create(text=text, blog=blog)
            comments = Comments.objects.filter(blog_id=id)
            return render(request, 'blog_detail.html', context={'blog': blog, "comments": comments})
    elif request.method == "GET":
        comments = Comments.objects.filter(blog_id=id)
        return render(request, 'blog_detail.html', context={'blog': blog, "comments": comments})


def create_blog(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        title = data["title"]
        image = files["image"]
        description = data['description']
        blog = Blog.objects.create(title=title, description=description, image=image)
        return render(request, 'blog_create).html')
    elif request.method == 'GET':
        return render(request, 'blog_form.html')


def form(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f'Your name: {first_name} , and last name: {last_name}')
    elif request.method == "GET":
        return render(request, 'form.html')


def change_view(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        return render(request, "blog_error.html")
    if request.method == "POST":
        data = request.POST
        file = request.FILES
        if data.get("title"):
            blog.title = data["title"]
        if data.get("description"):
            blog.description = data["description"]
        if file.get("image"):
            blog.image = file["image"]

        blog.save()
        return redirect(f"/blog/{blog.id}")
    elif request.method == "GET":
        context = {"blog": blog, "id": id}
        return render(request, "blog_change.html", context)
