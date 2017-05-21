from django.contrib import admin
from .models import Article, Categroy, Comments, Tag


class ArticleAdmin(admin.ModelAdmin):
	'''文章后台管理站点'''
	list_display = ('id','title','created','status','topped','abstract','categroy')
	#后台显示信息清单


class CategroyAdmin(admin.ModelAdmin):
	'''博客文章分类后台站点'''
	list_display = ('id','theme','created')


class CommentAdmin(admin.ModelAdmin):
	'''评论后台u案例站点'''
	list_display = ('name', 'article', 'comment_time','active')
	#定义显示属性的内容包含的内容
	list_filter = ('active', 'comment_time')
	#list_filter属性，实现简单的过滤功能
	search_fields = ('name',  'body')
    #通过使用search_fields属性定义了一个搜索字段列

class TagAdmin(admin.ModelAdmin):
	'''为标签模型建立后台管理站点'''
	list_display =('id', 'name', 'created_time', 'last_modified_time')

    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Categroy,CategroyAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Tag, TagAdmin)


