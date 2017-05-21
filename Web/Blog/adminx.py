
from .models import Article, Categroy, Comments, Tag
import xadmin

class Articleadmin(object):
	'''文章后台管理站点'''
	list_display = ('id','title','created','status','topped','abstract','categroy')
	#后台显示信息清单


class Categroyadmin(object):
	'''博客文章分类后台站点'''
	list_display = ('id','theme','created')


class Commentadmin(object):
	'''评论后台u案例站点'''
	list_display = ('name', 'article', 'comment_time','active')
	#定义显示属性的内容包含的内容
	list_filter = ('active', 'comment_time')
	#list_filter属性，实现简单的过滤功能
	search_fields = ('name',  'body')
    #通过使用search_fields属性定义了一个搜索字段列

class Tagadmin(object):
	'''为标签模型建立后台管理站点'''
	list_display =('id', 'name', 'created_time', 'last_modified_time')

    
xadmin.site.register(Article,Articleadmin)
xadmin.site.register(Categroy,Categroyadmin)
xadmin.site.register(Comments,Commentadmin)
xadmin.site.register(Tag, Tagadmin)


