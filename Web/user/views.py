from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def logout_view(request):
	#定义注销的视图
	logout(request)  # 请求注销
	return HttpResponseRedirect('/') # 返回跳转到index 页面


def register(request):
	'''定义函数实现注册新用户功能'''
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		# 处理填好的表单
		form =UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#让用户自动登录，再重定向到主页
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context = {'form': form}
	return  render (request, 'user/register.html', context)


def login_site(request):
	if request.method == 'post':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'registration/login.html', {
				'login_err': 'Please recheck your username or password !'
			})
	return render(request, 'registration/login.html')