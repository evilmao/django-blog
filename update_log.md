#### update log--项目进度更新明细
###
##### 按时间排序：
___
* **03/05/2017--**
  1. Bug修复：首页搜索框输入关键字后，无法执行搜索跳转
   	 * 操作方法：将首页中搜索框form标签修改成下面
          ```html
           <a id="search-menu" href="#">
               <span id="search-icon" class="ion-ios-search-strong"></span>
           </a>
           <div id="search-form" class="search-form">
                 <form role="search" method="get" id="searchform" action="/search/">
                      <input  type="text" name="q" placeholder="search" required><!--修改-->
                      <!--<input type="search" placeholder="Search" required>删除-->
                       <button type="submit">
                        <span class="ion-ios-search-strong"></span>
                       </button>
                 </form>
               </div>
          </div>
           
  2.  优化搜索结果展示页面。
    	* 修改位于searche/searche.html下的代码。详情代码参见文件。
   	  * **存在问题：搜索结果暂时无法进行分页**
___
* **02/05/2017--**
    1.  作者在登录的状态下可以对文章 ”删除“ 操作。
          * 操作方法：
        ①编辑views.py---在129行（文章修改视图）之后添加如下代码
            ```python
            def remove_article(request, pk):
              '''删除文章视图'''
              article = get_object_or_404(Article, pk=pk)
              article.delete()
              return HttpResponseRedirect(reverse('Blog:index'))
            ```
           	**说明：删除操作，直接使用数据库中delete()方法，不需要对应URL进行删除操作**
          ②在detail.html第29行（文章修改）之后添加以下代码：
            ```html
            <li class="active">
             <a class="btn btn-default" href="{% url 'Blog:remove_article' pk=article.pk %}">
              <span class="glyphicon glyphicon-remove">删除</span>
             </a>
            </li>
            ```

___
* **01/05/2017--**
  1. 新增备忘录功能：
  	 * 操作方法：在Web 应用下新建一个新的app,取名 todo
     输入指令：
       ```python
         python manage.py startapplication todo   #创建app项目
       ```
       记得创建app后在Web项目下setting.py文件中  INSTALLED_APPS中加入应用名，具体代码块，参见项目
       最后，做数据库迁移
   2. Bug修复 对登录注销的URL进行修改，修复个页面之间跳转导致的url无法识别问题。
    	 * 操作方法 ：如下
         ```python
         #登录页面
         url(r'^login/$', login, {'template_name': 'user/index.html'}, name='login'), #启用此url
         #url(r'^login/$', django.contrib.auth.views.login, name='login')弃用此url
         ```
       之后，再在相关页面中设置各个跳转页面的url地址，如果不是动态URL,建议使用绝对路径（url中绝对路径和相对路径请自行Google,或者参考[A标签href属性的相对路径与绝对路径](http://www.52jb.net/wangye/367.html)）
  3. 对分页进行美化：
   * 操作方法 ：
       使用第三方css代码进行优化，只需要修改templates/pagination.html下相应位置。         
 ___

* **30/04/2017--**
   1. Bug修复 : 优化首页’注销‘显示问题
      	 *  操作方法 : 将base.html第55行代码修改如下           
            ```  html 
            <li class="cl-effect-11"
            <a href="accounts/logout" data-hover="注销"> 注销</a>
            </li>
            ```

        * ‘修改文章’位置更正
           说明： 修改谋篇文章的操作提示不应该放在博客首页，应该将代码放置在谋篇文章的详情页面下； 只有是作者才可以对文章进行修改。
           操作方法: 
            ① 删除base.html中99-100行的代码；
            ②在detail.html 第20行代码后加入以下代码
           ```html  
              <ul class="nav nav-pills">
             {% if user.is_authenticated %} 
               <li class="active">
               <a class="btn btn-default" href="{% url 'Blog:edit_article' pk=article. %}">
                 <span class="glyphicon glyphicon-pencil">修改
                 </span>
               </a> 
               </li>
             {% endif %}
             </ul>
           ```
___

 * **29/04/2017--**     
    1.  添加分页效果 ：在首页，分类详情页面固定显示几篇最近发布的文章
        * **修改位置:  在index.html，catetroy_detail.html插入分页效果。参考[链接](http://www.jianshu.com/p/6c4615751854)**
        * **注意细节：**
           ①因我们自己的Blog之前已经创建过模板标签所以这里请直接	将paginator函数代码放置在 Blog/templatestags/blog_tags.py下。<br>
             ②新增代码编辑后，建议查看views.py下的关于变量的命名。参考文档中有矛盾。统一使用post_list或者article_list( 建议使用article_list)因在models中定义的是Article.
        * **存在问题：**
          目前无法以高亮展示在当前页面，界面不太美观，建议后期优化。
     2. 添加 "修改文章" 的时候需要登录验证
        * **修改位置:** 修改Web 文件夹下的urls.py  accounts 的setting LOGIN_REDIRECT_URL = '/' 登录后重新定向到首页。
     3. 首页显示优化：" 最新文章 "展示效果优化，搜索框可以直接跳出输入搜索关键字
        * **修改位置:** 修改base.html文件

          ```	html
          <script src="js/script.js"></script>     删除
          ```
          ``` html
          <script src="{% static 'blog/js/script.js' %}"></script>  19行处增加
          ```
         * **存在问题：搜索框跳出 ,键入关键字后，无法进行搜索**
___
 * **28/04/2017--**    
    1.  代码高亮:在文章编辑的时候和用户评论的时候可以是显示代码高亮度显示
       * **安装包:** pip install markdown pygments (参考[链接](http://www.cnblogs.com/felo/p/6480976.html))
         * **修改位置:** 
            1.在templatetags  blog_tags.py中添加custom_markdown功能 删除原有的	markdown功能 

         2.detail.html,index.html 评论中markdown部分,

         3.css中添加code.css

         4.base.html 中添加css的位置索引

          
___

 	


