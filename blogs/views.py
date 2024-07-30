from django.shortcuts import render
from django.core.paginator import Paginator
from blogs.models import post,caterory


def home(request):
    posts=post.objects.all()[:10]
    cats=caterory.objects.all().order_by('title')[:3]
   
    data={
        'posts':posts,
        'cats':cats,
    }

    return render(request,'home.html',data)
def base(request):
    return render(request,'base.html',{})

def posts(request,url):
    posts=post.objects.filter( url= url)
    cats=caterory.objects.all()
    # print(posts)

    return render(request,'post.html',{'posts':posts,'cats':cats})

def category(request,url):
    cat=caterory.objects.get(url=url)
    posts=post.objects.filter(cat=cat)

    return render(request,'category.html',{'cat':cat,'posts':posts})