"""定义learning_logs的URL模式"""
# 导入函数url来将URL映射到视图
# 导入模块views，其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图
from django.urls import re_path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    # 实际的URL模式是一个对函数url()的调用，这个函数接受三个实参
    # 第一个是一个正则表达式。Django在urlpatterns中查找与请求的URL字符串匹配的正则表达式，因此正则表达式定义了Django可查找的模式。
    # r让Python将接下来的字符串视为原始字符串，而引号告诉Python正则表达式始于和终于何处。脱字符（^）让Python查看字符串的开头，而美元符号让Python查看字符串的末尾
    # '^$'正则表达式让Python查找开头和末尾之间没有任何东西的URL。Python忽略项目的基础URL（http://localhost:8000/），因此这个正则表达式与基础URL匹配。其他URL都与这个正则表达式不匹配。如果请求的URL不与任何URL模式匹配，Django将返回一个错误页面。
    # url()的第二个实参指定了要调用的视图函数。请求的URL与前述正则表达式匹配时，Django将调用views.index
    # 第三个实参将这个URL模式的名称指定为index，让我们能够在代码的其他地方引用它。每当需要提供到这个主页的链接时，我们都将使用这个名称，而不编写URL。
    re_path(r'^$', views.index, name='index'),
    # 显示所有的主题
    # 可以在末尾包含斜杠，也可以省略它，但单词topics后面不能有任何东西，否则就与该模式不匹配
    re_path(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    # /(?P<topic_id>\d+)/）与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为topic_id的实参中。这部分表达式两边的括号捕获URL中的值；?P<topic_id>将匹配的值存储到topic_id中；而表达式\d+与包含在两个斜杆内的任何数字都匹配，不管这个数字为多少位。
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]