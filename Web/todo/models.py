from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
	user = models.ForeignKey(User)
	todo = models.CharField(max_length=50)
	flag = models.CharField(max_length=2)
	priority = models.CharField(max_length=2)
	pubtime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%d %s %s' % (self.id, self.todo, self.flag)

	class Meta:
		ordering = ['priority', 'pubtime']