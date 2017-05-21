from django import forms
from .models import Comments, Article


class CommentForm(forms.ModelForm):
	'''用户评论表单'''
	class Meta:
		'''继承Comments数据模型'''
		model = Comments
		fields = ('name','comment_body' )
		widgets = {'comment_body': forms.Textarea(attrs={'cols':60})}


class ArticleAddForm(forms.ModelForm):
	'''文章编辑表单，使管理员可以直接在客户端进行操作'''
	class Meta:
		'''继承Article数据模型'''
		model = Article
		fields = ('title','author','categroy','status','tags','body','topped')
		widgets = {'body': forms.Textarea(attrs={'cols':80})}
		help_texts = {
			'tags':("(按住'Control',或者Mac上的'Command'，可以选择多个.)"),
		}
					
