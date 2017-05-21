import datetime
from haystack import indexes                          #导入haystack模块中的indexes函数
from Blog.models import Article                       #要指定出搜索的对象，这里我们是要搜索所有的博客文章
from jieba.analyse import ChineseAnalyzer


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    '''定一个类，用来进行文章搜索'''
    text = indexes.CharField(document=True, use_template=True)
    '''
        定义text字段，每个索引里面必须有且只能有一个字段为document=True
        这代表haystack 和搜索引擎将使用此字段的内容作为索引进行检索。
        haystack提供了use_template=True，允许我们使用数据模板去建立搜索
        引擎索引的文件
    '''
    author = indexes.CharField(model_attr='author')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
    	#定义方法属性
        return Article
        #返回Article模块

    def index_queryset(self, using=None):
        """当整个模型索引更新时使用"""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())