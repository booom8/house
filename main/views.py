from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Comment
from .forms import CommentForm

def home(request):
    prods = Product.objects.all()
    menu = Product.objects.all()
    return render(request, 'main/main.html', {'prods' : prods,}) #'menu' : menu})

def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def post_category(request, url):
    prods = Product.objects.filter(category__url=url)
    menu = Product.objects.all()
    return render(request, 'main/main.html', {'prods' : prods,}) #'menu' : menu})

def post_detail(request, pk):
    prod = get_object_or_404(Product, id=pk)
    comment = Comment.objects.filter(prod=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name_id = request.user.id
            form.prod_id = prod.id
            form.save()
    else:
        form = CommentForm()

    return render(request, 'main/house_detail.html', {
        "prod":prod,
        "comment":comment,
        "form":form
        })
