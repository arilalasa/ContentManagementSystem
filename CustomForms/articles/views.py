# Create your views here.
from django.shortcuts import render_to_response
from articles.models import Article
from articles.form import ArticleForm,LoginForm,RegisterForm
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import datetime

def home_page(request):
    article_list = Article.objects.all()
    context_variables = RequestContext(request,{'list':article_list})
    return render_to_response('articles.html',locals(),context_variables)

def home(request,article_id=None):
    article_obj=None
    if article_id:
        article_obj = Article.objects.get(id = article_id)
        user=User.objects.get(id = request.session['id'])
    
    if request.method == 'POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if article_id:
                article_obj.title = title
                article_obj.content = content
                article_obj.modified_at = datetime.datetime.now()
                article_obj.save()
            else:
                insert_db=Article(title = form.cleaned_data['title'],
                                  content = form.cleaned_data['content'],
                                  created_by=request.session['username'],
                                 )
                insert_db.save()
            return HttpResponseRedirect('/') 
    else:
        if article_id:
            if (user.is_superuser or (article_obj.created_by == request.session['username'])):
                form=ArticleForm(initial = {'title': article_obj.title,'content' : article_obj.content})
            else:
                return HttpResponseRedirect('/')
        else:
             form = ArticleForm()
    context_variables = RequestContext(request)
    return render_to_response('article_index.html',locals(),context_variables)

def delete(request,article_id):
    articleobj=Article.objects.get(id=article_id)
    articleobj.delete()
    return HttpResponseRedirect('/')

def auth_login(request):
    if request.method=='POST':
        userid=request.POST['userid']
        password=request.POST['password']
        user=authenticate(username=userid,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                m=User.objects.get(username=request.POST['userid'])
                request.session['username']=userid
                request.session['id']=m.id
                return HttpResponseRedirect('/')
            else:
                return render_to_response('login.html',{'error_message':'Disable account'})
        else:
            form=LoginForm()
            context_variables=RequestContext(request,{'error_message':'Invalid login'})
    else:
        form = LoginForm()
        context_variables = RequestContext(request)
    return render_to_response('login.html',locals(),context_variables)

def auth_logout(request):
    logout(request)
    #del request.session['id']
    #del request.session['username']
    form = LoginForm()
    context_variables = RequestContext(request)
    return render_to_response('login.html',locals(),context_variables)


def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            newuser=form.save1()
            return HttpResponseRedirect('/home')
  
    else:
        form=RegisterForm()
    return render_to_response('register.html',{'form':form})

      
