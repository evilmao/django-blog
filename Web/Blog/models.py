from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone

class Categroy(models.Model):
	'''文章分类'''
	theme = models.CharField('文章分类',max_length=10)
	created = models.DateTimeField('创建时间',auto_now_add=True)

	class Meta:
		ordering =('-created',)
		verbose_name_plural = '文章分类'

	def __str__(self):
		return self.theme


class  Tag(models.Model):
	'''标签数据管理模型'''
	name = models.CharField(max_length=20)
	created_time = models.DateTimeField('创建时间', auto_now_add=True)
	last_modified_time = models.DateTimeField('修改时间', auto_now=True)

	class Meta:
		verbose_name_plural = '标签管理器'

	def __str__(self):
		return self.name


class Article(models.Model):
	'''文章详情数据模型'''
	categroy = models.ForeignKey(Categroy,verbose_name='分类', on_delete=models.CASCADE)
	STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('personal','Personal'),
    )
	title = models.CharField('标题',max_length=70)
	created = models.DateTimeField('创建时间', auto_now_add=True)
	updated = models.DateTimeField('更新时间', auto_now=True)
	status = models.CharField('文章状态', max_length=10, choices=STATUS_CHOICES, default='draft')
	author = models.ForeignKey(User,verbose_name='作者')
	slug = models.SlugField('标签', max_length=250, unique_for_date='created')
	body = models.TextField('正文')
	topped = models.BooleanField('置顶', default=False)
	views = models.PositiveIntegerField('浏览量', default=0)
	likes = models.PositiveIntegerField('点赞数', default=0)
	abstract = models.CharField('摘要', max_length=7, blank=True, null=True, 
                                help_text="可选，如若为空将摘取正文的前54个字符")
	#此功能暂时无法实现
	tags = models.ManyToManyField(Tag, verbose_name='标签集合',blank=True)
	'''
		对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用
	 	ManyToManyField，表明这是多对多的关联关系。同时我们规定文章可以没有标签，因此为
	 	标签tags 指定了 blank=True。使用through参数指向像中间人一样工作的模型,从而可以在
	 	数据库中进行增加，创建 新的对象。
	'''	
	class Meta:
		ordering = ('-created',)
		verbose_name_plural = '文章'
		
	def __str__(self):
		return self.title
	"""
		def get_absolute_url(self):
		    path = reverse('detail', kwargs={'pk': self.id})
		    return "http://192.168.1.17:8000%s" % path
	 """

	def get_absolute_url(self):
		return reverse('Blog:detail', kwargs={'pk': self.pk})


class Comments(models.Model):
	'''评论管理数据模型'''
	article = models.ForeignKey(Article, verbose_name='文章评论',related_name='comments')
	comment_body = models.TextField('内容')
	comment_time = models.DateTimeField('评论时间',auto_now=True)
	name = models.CharField('昵称',max_length=10)
	active = models.BooleanField(default=True)
	#comment_response = models.TextField('评论回复')
	#comment_like = models.PositiveIntegerField('点赞数', default=0)

	class Meta:
		ordering = ('comment_time',)
		verbose_name_plural = '评论管理'

	def __str__(self):
		 return 'Comment by {} on {}'.format(self.name, self.article)




			





		


