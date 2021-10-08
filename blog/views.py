import random


from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog

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
        return render(request, 'blog_detail.html', context={'blog': blog})
    except Exception:
        return render(request, "blog_error.html")


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
