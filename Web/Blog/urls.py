from django.conf.urls import url,include
from haystack.views import SearchView
from jieba.analyse import ChineseAnalyzer
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
    #文章详情页面
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #按日期归档页面
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.Archives, name='Archives'),
    #按主题分类页面
    url(r'^category/(?P<pk>[0-9]+)/$', views.categroy_detail, name='category'),  
    #搜索视图页面
    url(r'^search/', include('haystack.urls')),
    #about视图页面
    url(r'^about', views.about_me, name='about'),
    #新增文章视图页面
    url(r'^new_article/$', views.new_article, name='new_article'),
    #编辑文章
    url(r'^edit_article/(?P<pk>[0-9]+)/$', views.edit_article, name='edit_article'),
    #删除谋篇文章
    url(r'^remove_article/(?P<pk>[0-9]+)/$', views.remove_article, name='remove_article'),
    #为标签视图添加url
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tag_categroy, name='tag_categroy'),
    
]