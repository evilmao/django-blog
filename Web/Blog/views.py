
from Blog.models import Article ,Comments ,Categroy,Tag
from django.contrib.auth.decorators import login_required 
from django.core.urlresolvers import reverse
from django.db.models import Count 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views.generic.list import ListView           #继承自ListVIew，用于展示从数据库中获取的文章列表
from django.shortcuts import redirect
from .forms import CommentForm, ArticleAddForm
import markdown2


def index(request):
    """定义主页视图"""
    article_list = Article.objects.all()
    context = {'article_list': article_list}

    return render(request, 'blog/index.html',context)


def Archives(request,year,month):
    '''定义视图用来实现按年月进行归档'''
    article_list = Article.objects.filter(created__year=year, 
						                  created__month=month,
                                          )
    #调用Article模型的数据库，通过fitler过滤器，created属性来过滤出文章年月的排序进行归档
    context = {'article_list': article_list}

    return render(request, 'blog/index.html', context)
    #返回模板视图。


def Category(request, pk):
    """
    定义分类视图函数，用来文章归类
    """
    cate = get_object_or_404(Category, pk=pk)
    article_list = Categroy.objects.filter(theme=cate)
    context={'article_list': article_list}

    return render(request, 'blog/index.html',  context)
                 


def detail(request, pk):
    """文章详情页"""
    article = get_object_or_404(Article, pk=pk)
    body = Article.objects.get(pk=pk)
    comments = article.comments.filter(active=True)
    #添加了一个查询集（QuerySet）来获取这个帖子所有有效的评论，通过参数过滤所有已经发布过的
    new_comment = None
    #定义一个变量名为new_comment 及为新的评论 为 空

    if request.method == 'POST':
         # 如果是通过POST请求，我们使用提交的数据新建一条评论
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 用is_valid()方法验证这些数据去实例化表单，如果表单通过验证，我们会做以下的操作：
            new_comment = comment_form.save(commit=False)
            '''
            通过调用表单的save()方法创建一个新的Comment对象，参数执行使对象无法立即保存到数据库中。
            注意save()方法是给ModelForm用的，而不是给Form实例用的
            '''
            new_comment.article = article
             #为刚创建的评论分配到当前的帖子
            new_comment.save()
            # 再次执行保存，这次是保存到数据库中的
    else:
        #通过GET请求被加载的，那么我们用comment_fomr = commentForm()来创建一个表单实例。
        comment_form = CommentForm()

    context = {'article': article,
               'comments':comments,
               'body':body,
               'comment_form':comment_form}

    return render(request, 'blog/detail.html', context )


"""def new_article(request):
    if request.method == 'POST':
        form = ArticleAddForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.auther = request.user
            article.save()
            return redirect(detail, pk=article.pk)
    else:
        form = ArticleAddForm()

    context = {'form': form}
    return render(request, 'blog/new_article.html',context)"""


def new_article(request):
    '''新增文章视图(操作时，一定要后台登录以后才能进行操作)'''
    if request.method != "POST":
        form = ArticleAddForm()
    else:
        form = ArticleAddForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            #提交后建议跳转到文章详情(detail)页面
            return HttpResponseRedirect(reverse('Blog:index'))
          
    context = {'form': form}
    return render(request, 'blog/new_article.html', context)



def edit_article(request, pk):
    '''对谋篇文章编辑视图'''
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = ArticleAddForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            '''
                由于Tag和Article模型为ManytoMany.当使用commit=False的时候。Django 不会立即为多对多关系保存表单
                数据。这是因为只有实例在数据库中存在时才可以保存实例的多对多数据。此时Django将添加一个save_m2m() 
                方法到你的模型表单子类。在你手工保存有表单生成的实例之后，你可以调用save_m2m() 来保存多对多的表单数据
            '''
            
            return HttpResponseRedirect(reverse('Blog:index'))
            #建议修改文章后返回当前文章详情(detail)页面
    else:
        form = ArticleAddForm(instance=article)

    context = {'form': form}
    return render(request, 'blog/edit_article.html', context)


def remove_article(request, pk):
    '''删除文章视图'''
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponseRedirect(reverse('Blog:index'))


def categroy_detail(request,pk):
    '''分类标签文章详情'''
    categroy_title = Categroy.objects.get(pk=pk)
    article_list = categroy_title.article_set.order_by('-created') 
    context = {'categroy_title': categroy_title,
               'article_list': article_list
               }

    return render(request, 'blog/categroy_detail.html', context )


def about_me(request):
    '''定义首页about_me视图'''
    return render(request, 'blog/about.html')


def  tag_categroy(request,pk):
    ''' 定义标签分类详情函数  '''
    tag = get_object_or_404(Tag,pk=pk)
    article_list = Article.objects.filter(tags__in=[tag])
    context = {'tag':tag, 'article_list':article_list}

    return render(request, 'blog/tag_categroy.html',  context)




