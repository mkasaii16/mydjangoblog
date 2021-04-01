from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = models.Articles.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request,'articles/articleslist.html',args)

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url = "/account/login")
#baraye chek kardane login
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/create_article.html',{'form':form})
