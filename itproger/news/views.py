from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticlesForm
from django.http import HttpResponse

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            news_item = form.save()
            if 'image' in request.FILES:
                news_item.image = request.FILES['image']
            news_item.save()    
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
            print(form.error)
    else:
        form = ArticlesForm()
    
    return render(request, 'news/create.html', {'form': form, 'error' : error})

def news_detail(request, news_id):
    article = get_object_or_404(Articles, id = news_id)
    return render(request, 'news/news_detail.html', {'article': article})
