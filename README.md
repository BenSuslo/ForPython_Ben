# ForPython_Ben

# name: SU
# time: 2022/02/24
# project: Django
在本章中，你将学习如何使用Django（http://djangoproject.com/）来开发一个名为“学习笔记”（Learning Log）的项目，这是一个在线日志系统，让你能够记录所学习的有关特定主题的知识。

Django是一个Web框架——一套用于帮助开发交互式网站的工具。Django能够响应网页请求，还能让你更轻松地读写数据库、管理用户等。

<!-- 建立项目时，首先需要以规范的方式对项目进行描述，再建立虚拟环境，以便在其中创建项目。 -->

要使用Django，首先需要建立一个虚拟工作环境。虚拟环境是系统的一个位置，你可以在其中安装包，并将其与其他Python包隔离。将项目的库与其他项目分离是有益的，且为了在第20章将“学习笔记”部署到服务器，这也是必须的。
为项目新建一个目录，将其命名为learning_log，再在终端中切换到这个目录，并创建一个虚拟环境。如果你使用的是Python3，可使用如下命令来创建虚拟环境：
learning_log$python -m venv ll_env
learning_log$
这里运行了模块venv，并使用它来创建一个名为ll_env的虚拟环境。
建立虚拟环境后，需要使用下面的命令激活它：
learning_log$source ll_env/bin/activate
(ll_env)learning_log$
这个命令运行ll_env/bin中的脚本activate。环境处于活动状态时，环境名将包含在括号内。在这种情况下，你可以在环境中安装包，并使用已安装的包。你在ll_env中安装的包仅在该环境处于活动状态时才可用。
<!-- 注意 -->
　如果你使用的是Windows系统，请使用命令ll_env\Scripts\activate（不包含source）来激活这个虚拟环境。
<!--  -->
要停止使用虚拟环境，可执行命令deactivate：
(ll_env)learning_log$deactivate
learning_log$
如果关闭运行虚拟环境的终端，虚拟环境也将不再处于活动状态。 ###**18.1.5　安装Django**创建并激活虚拟环境后，就可安装Django了：
(ll_env)learning_log$pip install Django
...
(ll_env)learning_log$
由于我们是在虚拟环境中工作，因此在所有的系统中，安装Django的命令都相同：不需要指定标志--user，也无需使用python -m pip install package_name这样较长的命令。别忘了，Django仅在虚拟环境处于活动状态时才可用。
<!-- 
    将Django安装到F:\VScode_workspace\VSCode_for_Python\Django\learning_log
 -->

 在依然处于活动的虚拟环境的情况下（ll_env包含在括号内），执行如下命令来新建一个项目：
 <!-- 新建一个名为learning_log的项目。这个命令末尾的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器。 -->
(ll_env)learning_log$django-admin startproject learning_log .
(ll_env)learning_log$ls
learning_log ll_env manage.py
(ll_env)learning_log$ls learning_log
__init__.py settings.py urls.py wsgi.py
<!-- 注意　千万别忘了这个句点，否则部署应用程序时将遭遇一些配置问题。如果忘记了这个句点，就将创建的文件和文件夹删除（ll_env除外），再重新运行这个命令。 -->
<!-- windows系统里不能用ls指令，而要用dir指令 -->
目录learning_log包含4个文件，其中最重要的是settings.py、urls.py和wsgi.py。文件settings.py指定Django如何与你的系统交互以及如何管理项目。在开发项目的过程中，我们将修改其中一些设置，并添加一些设置。文件urls.py告诉Django应创建哪些网页来响应浏览器请求。文件wsgi.py帮助Django提供它创建的文件，这个文件名是web server gatewayinterface（Web服务器网关接口）的首字母缩写。

Django将大部分与项目相关的信息都存储在数据库中，因此我们需要创建一个供Django使用的数据库。为给项目“学习笔记”创建数据库，请在处于活动虚拟环境中的情况下执行下面的命令：
(ll_env)learning_log$python manage.py migrate
Operations to perform:❶
Apply all migrations: admin,auth,contenttypes,sessions
Running migrations:
Applying contenttypes.0001_initial.. . OK
Applying auth.0001_initial... OK
--snip--
(ll_env)learning_log$ls
dp.sqlite3 learning_log ll_env manage.py
<!-- windows系统里不能用ls指令，而要用dir指令 -->
我们将修改数据库称为迁移数据库。首次执行命令migrate时，将让Django确保数据库与项目的当前状态匹配。在使用SQLite（后面将更详细地介绍）的新项目中首次执行这个命令时，Django将新建一个数据库。
在❶处，Django指出它将创建必要的数据库表，用于存储我们将在这个项目（Synchronize unmigratedapps，同步未迁移的应用程序）中使用的信息，再确保数据库结构与当前代码（Apply all migrations，应用所有的迁移）匹配。
SQLite是一种使用单个文件的数据库，是编写简单应用程序的理想选择，因为它让你不用太关注数据库管理的问题。

下面来核实Django是否正确地创建了项目。为此，可执行命令runserver，如下所示：
(ll_env)learning_log$python manage.py runserver
Watching for file changes with StatReloader
Performing system checks. . .
System check identified no issues (0 silenced).❶
February 24，2022- 21:16:51
Django version 4.0.2，using settings 'learning_log.settings'❷
Starting development server at http://127.0.0.1:8000/❸
Quit the server with CTRL一BREAK.
Django启动一个服务器，让你能够查看系统中的项目，了解它们的工作情况。当你在浏览器中输入URL以请求网页时，该Django服务器将进行响应：生成合适的网页，并将其发送给浏览器。
在❶处，Django通过检查确认正确地创建了项目；在❷处，它指出了使用的Django版本以及当前使用的设置文件的名称；在❸处，它指出了项目的URL。URL http://127.0.0.1:8000/表明项目将在你的计算机（即localhost）的端口8000上侦听请求。localhost是一种只处理当前系统发出的请求，而不允许其他任何人查看你正在开发的网页的服务器。
现在打开一款Web浏览器，并输入URL：http://localhost:8000/；如果这不管用，请输入http://127.0.0.1:8000/。你将看到类似于图18-1所示的页面，这个页面是Django创建的，让你知道到目前为止一切正常。现在暂时不要关闭这个服务器。若要关闭这个服务器，按Ctrl+C即可。
注意　如果出现错误消息“That port is already in use”（指定端口已被占用），请执行命令python manage.pyrunserver 8001，让Diango使用另一个端口；如果这个端口也不可用，请不断执行上述命令，并逐渐增大其中的端口号，直到找到可用的端口。



# 创建应用程序
Django项目由一系列应用程序组成，它们协同工作，让项目成为一个整体。
再打开一个终端窗口（或标签页），并切换到manage.py所在的目录。激活该虚拟环境，再执行命令startapp(以Windows系统为例)：
learning_log$ll_env\Scripts\activate
(ll_env)learning_log$python manage.py startapp learning_logs
(ll_env)learning_log$dir
dp.sqlite3 learning_log learning_logs ll_env manage.py
(ll_env)learning_log$dir learning_logs\
<!-- Windows目录用\，Linux系统用/ -->
命令startappappname让Django建立创建应用程序所需的基础设施。如果现在查看项目目录，将看到其中新增了一个文件夹learning_logs（见❶）。打开这个文件夹，看看Django都创建了什么（见❷）。其中最重要的文件是models.py、admin.py和views.py。我们将使用models.py来定义我们要在应用程序中管理的数据。admin.py和views.py将在稍后介绍。

# 若遇到问题：Import "django.db" could not be resolved from
# 解决方法：将项目所在文件夹加入工作区即可。 
# 文件-》将文件夹添加到工作区



需要让Django修改数据库，使其能够存储与模型Topic相关的信息。为此，在终端窗口中执行下面的命令：
(ll_env)learning_log$python manage.py makemigrations learning_logs
...
(ll_env)learning_log$
命令makemigrations让Django确定该如何修改数据库，使其能够存储与我们定义的新模型相关联的数据。输出表明Django创建了一个名为0001_initial.py的迁移文件，这个文件将在数据库中为模型Topic创建一个表。
下面来应用这种迁移，让Django替我们修改数据库：
(ll_env)learning_log$python manage.py migrate
...
输出“Applying learning_logs.0001_initial... OK”即表示Django确认为learning_logs应用迁移时一切正常（OK）
<!-- 每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py；对learning_logs调用makemigrations；让Django迁移项目。 -->

# Django管理网站
# 创建超级用户
为在Django中创建超级用户，请执行下面的命令并按提示做：
(ll_env)learning_log$python manage.py createsuperuser
Username(leave blank to use 'asus'):ll_admin❶
Email address:❷
Password:❸
Password(again):
Superuser created successfully.
(ll_env)learning_log$
你执行命令createsuperuser时，Django提示你输入超级用户的用户名（见❶）。这里我们输入的是ll_admin，但你可以输入任何用户名，比如电子邮件地址，也可让这个字段为空（见❷）。你需要输入密码两次（见❸）。
<!-- 密码为dj123456 -->
注意　可能会对网站管理员隐藏有些敏感信息。例如，Django并不存储你输入的密码，而存储从该密码派生出来的一个字符串——散列值。每当你输入密码时，Django都计算其散列值，并将结果与存储的散列值进行比较。如果这两个散列值相同，就通过了身份验证。通过存储散列值，即便黑客获得了网站数据库的访问权，也只能获取其中存储的散列值，而无法获得密码。在网站配置正确的情况下，几乎无法根据散列值推导出原始密码。
# 向管理网站注册模型
Django自动在管理网站中添加了一些模型，如User和Group，但对于我们创建的模型，必须手工进行注册。
在admin.py注册后使用超级用户账户访问管理网站：访问http://localhost:8000/admin/，并输入你刚创建的超级用户的用户名和密码，你将看到类似于图18-2所示的屏幕。这个网页让你能够添加和修改用户和用户组，还可以管理与刚才定义的模型Topic相关的数据。



#
创建条目，输入一些数据后，就可通过交互式终端会话以编程方式查看这些数据了。这种交互式环境称为Django shell，是测试项目和排除其故障的理想之地。
在活动的虚拟环境中执行时，命令python manage.py shell启动一个Python解释器，可使用它来探索存储在项目数据库中的数据。在这里，我们导入了模块learning_logs.models中的模型Topic（见❶），然后使用方法Topic.objects.all()来获取模型Topic的所有实例；它返回的是一个列表，称为查询集（queryset）。
我们可以像遍历列表一样遍历查询集。

在简单的shell环境中排除故障要比在生成网页的文件中排除故障容易得多。

注意　每次修改模型后，你都需要重启shell，这样才能看到修改的效果。要退出shell会话，可按Ctr+D；如果你使用的是Windows系统，应按Ctr+Z，再按回车键。


Django API：编写访问项目中的数据的代码时，你编写的是查询。请浏览有关如何查询数据的文档，其网址为https://docs.djangoproject.com/en/7.8/topics/db/queries/。其中大部分内容都是你不熟悉的，但等你自己开发项目时，这些内容会很有用。

# 创建网页：学习笔记主页
使用Django创建网页的过程通常分三个阶段：定义URL、编写视图和编写模板。
首先，你必须定义URL模式。URL模式描述了URL是如何设计的，让Django知道如何将浏览器请求与网站URL匹配，以确定返回哪个网页。每个URL都被映射到特定的视图——视图函数获取并处理网页所需的数据。视图函数通常调用一个模板，后者生成浏览器能够理解的网页。

# 编写模板
模板定义了网页的结构。模板指定了网页是什么样的，而每当网页被请求时，Django将填入相关的数据。模板让你能够访问视图提供的任何数据。我们的主页视图没有提供任何数据，因此相应的模板非常简单。

django.conf.urls.url() 在 Django 3.0 中被弃用，在 Django 4.0+ 中被移除。
最简单的解决方法是将 url() 替换为 re_path()。 re_path 使用像 url 这样的正则表达式，因此您只需更新导入并将 url 替换为 re_path。
from django.urls import include, re_path
from myapp.views import home
urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^myapp/', include('myapp.urls'),
]
或者，您可以改用path。 path() 不使用正则表达式，因此如果您切换到路径，则必须更新您的 URL 模式。
from django.urls import include, path
from myapp.views import home
urlpatterns = [
    path('', home, name='home'),
    path('myapp/', include('myapp.urls'),
]
如果您有一个包含许多 URL 模式需要更新的大型项目，您可能会发现 django-upgrade 库对更新您的 url.py 文件很有用。
... Jetbrains 的最新 PyCharm 教程仍然使用 django.conf.urls。


<!-- 这个文件的第一部分创建一个包含项目名的段落，该段落也是一个到主页的链接。为创建链接，我们使用了一个模板标签，它是用大括号和百分号（{% %}）表示的。模板标签是一小段代码，生成要在网页中显示的信息。在这个实例中，模板标签{% url'learning_logs:index' %}生成一个URL，该URL与learning_logs/urls.py中定义的名为index的URL模式匹配（见❶）。在这个示例中，learning_logs是一个命名空间，而index是该命名空间中一个名称独特的URL模式。 -->
<!-- 子模板的第一行必须包含标签{% extends %}，让Django知道它继承了哪个父模板 -->

python3 Django 环境下，如果你遇到在根目录下urls.py中的include方法的第二个参数namespace添加之后就出错的问题。请在[app_name]目录下的urls.py中的urlpatterns前面加上app_name='[app_name]'， [app_name]代表你的应用的名称。

模板文档：请浏览Django模板文档，其网址为https://docs.djangoproject.com/en/1.8/ref/templates/。自己开发项目时，可再回过头来参考该文档。

Web应用程序的核心是让任何用户都能够注册账户并能够使用它，不管用户身处何方。在本章中，你将创建一些表单，让用户能够添加主题和条目，以及编辑既有的条目。你还将学习Django如何防范对基于表单的网页发起的常见攻击，这让你无需花太多时间考虑确保应用程序安全的问题。


在使用Django提供的默认登录视图来实现登录界面功能时出现报错：TypeError: login() got an unexpected keyword argument 'template_name’
原来，作者使用的Django是版本是1.0的，其实现代码为：
from django.contrib.auth import login
url(r'^login/$', login, { 'template_name'='users/login.html' },name='login ')
但是，在Django2.0中内置登陆视图不再是函数，而是类，位置在django.contrib.auth.views.LoginView，具体实现为：
from django.conf.urls import url
from django.contrib.auth.views import LoginView
urlpatterns = [
#登录界面   LoginView.as_view后面要加上()
url(r'login/$ ' ,LoginView.as_view(template_name='users/login.html ' ) ,name='login')
]


# 注册用户
用户名：Suslo_1
密码：Su561847


owner = models.ForeignKey(User)出现错误 TypeError: init() missing 1 required positional argument: ‘on_delete’
解决办法：
改为
owner = models.ForeignKey(User, on_delete=models.CASCADE)


注意　你可以重置数据库而不是迁移它，但如果这样做，既有的数据都将丢失。一种不错的做法是，学习如何在迁移数据库的同时确保用户数据的完整性。如果你确实想要一个全新的数据库，可执行命令python manage.py flush，这将重建数据库的结构。如果你这样做，就必须重新创建超级用户，且原来的所有数据都将丢失。


Bootstrap库，这是一组工具，用于为Web应用程序设置样式，使其在任何现代设备上都看起来很专业，无论是大型的平板显示器还是智能手机。
把项目“学习笔记”部署到Heroku，这个网站让你能够将项目推送到其服务器，让任何有网络连接的人都可使用它。我们还将使用版本控制系统Git来跟踪对这个项目所做的修改。

Bootstrap基本上就是一个大型的样式设置工具集，它还提供了大量的模板，你可将它们应用于项目以创建独特的总体风格。对Bootstrap初学者来说，这些模板比各个样式设置工具使用起来要容易得多。要查看Bootstrap提供的模板，可访问http://getbootstrap.com/，单击Getting Started，再向下滚动到Examples部分，并找到Navbars in action。我们将使用模板Static top navbar，它提供了简单的顶部导航条、页面标题和用于放置页面内容的容器。




base.html初版内容：
<!-- 创建网站时，几乎都有一些所有网页都将包含的元素。在这种情况下，可编写一个包含通用元素的父模板，并让每个网页都继承这个模板，而不必在每个网页中重复定义这些通用元素。 -->
<!-- 在简单的HTML页面中，链接是使用锚标签定义的：
        <a href="link_url">link text</a>
-->
<!-- 让模板标签来生成URL，可让链接保持最新容易得多。要修改项目中的URL，只需修改urls.py中的URL模式，这样网页被请求时，Django将自动插入修改后的URL。在我们的项目中，每个网页都将继承base.html，因此从现在开始，每个网页都包含到主页的链接。 -->
<!-- 我们插入了一对块标签。这个块名为content，是一个占位符，其中包含的信息将由子模板指定。子模板并非必须定义父模板中的每个块，因此在父模板中，可使用任意多个块来预留空间，而子模板可根据需要定义相应数量的块。 -->
<!-- 注意　在Python代码中，我们几乎总是缩进四个空格。相比于Python文件，模板文件的缩进层级更多，因此每个层级通常只缩进两个空格。 -->
<!-- is_authenticated属性：如果用户已登录，该属性将为True，否则为False -->
<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a> -
    <a href="{% url 'learning_logs:topics' %}">Topics</a> - 
    {% if user.is_authenticated %}
      Hello, {{ user.username }}.
      <a href="{% url 'users:logout' %}">log out</a>
    {% else %}
      <a href="{% url 'users:register' %}">register</a> -
      <a href="{% url 'users:login' %}">log in</a>
    {% endif %}
</p>
{% block content %}{% endblock content %}


HTML文件分为两个主要部分：头部（head）和主体（body）
HTML文件的头部不包含任何内容：它只是将正确显示页面所需的信息告诉浏览器

login.html初版：
{% extends "learning_logs/base.html" %}
{% block content %}
  {% if form.errors %}
  <p>Your username and password didn't match. Please try again.</p>
  {% endif %}
  <form method="post" action="{% url 'users:login' %}">
  {% csrf_token %}
  {{ form.as_p }}
  <button name="submit">log in</button>
  <input type="hidden" name="next" value="{% url 'learning_logs:index' %}"/>
  </form>
{% endblock content %}



Heroku，这是一个基于Web的平台，让你能够管理Web应用程序的部署
# 建立Heroku账户
要建立账户，请访问https://heroku.com/，并单击其中的一个注册链接。注册账户是免费的，Heroku提供了免费试用服务，让你能够将项目部署到服务器并对其进行测试。
注意　Heroku提供的免费试用服务存在一些限制，如可部署的应用程序数量以及用户访问应用程序的频率。但这些限制都很宽松，让你完全能够在不支付任何费用的情况下练习部署应用程序。
# 安装Heroku Toolbelt
要将项目部署到Heroku的服务器并对其进行管理，需要使用Heroku Toolbelt提供的工具。要安装最新的Heroku Toolbelt版本，请访问https://toolbelt.heroku.com/，并根据你使用的操作系统按相关的说明做：使用只包含一行的终端命令，或下载并运行安装程序。
你还需安装很多包，以帮助在服务器上支持Django项目提供的服务。为此，在活动的虚拟环境中执行如下命令：
pip install dj-database-url
pip install dj-static
pip install static3
pip install gunicorn
dj-database-url包帮助Django与Heroku使用的数据库进行通信，dj-static和static3包帮助Django正确地管理静态文件，而gunicorn是一个服务器软件，能够在在线环境中支持应用程序提供的服务。（静态文件包括样式规则和JavaScript文件。）
注意　在Windows系统中，有些必不可少的包可能无法安装，因此如果在你尝试安装有些这样的包时出现错误消息，也不用担心。重要的是让Heroku在部署中安装这些包，下一节就将这样做。

注意　如果出现错误消息，指出不能使用你指定的Python版本，请访问https://devcenter.heroku.com/并单击Python，再单击链接Specifying a Python Runtime。浏览打开的文章，了解支持的Python版本，并使用与你使用的Python版本最接近的版本。

Procfile告诉Heroku启动哪些进程，以便能够正确地提供项目提供的服务。
web: gunicorn learning_log.wsgi --log-file -
这行代码让Heroku将gunicorn用作服务器，并使用learning_log/wsgi.py中的设置来启动应用程序。标志log-file告诉Heroku应将哪些类型的事件写入日志。

在Heroku上，Django搜集所有的静态文件，并将它们放在一个地方，以便能够高效地管理它们。我们将创建一个用于存储这些静态文件的目录。在文件夹learning_log中，有一个名称也为learning_log的子文件夹。在这个子文件夹中，新建一个名为static的文件夹，因此这个文件夹的路径为learning_log/learning_log/static/。我们还需在这个文件夹中创建一个占位文件，因为项目被推送到Heroku时，它将不会包含原来为空的文件夹。在目录static/中，创建一个名为placeholder.txt的文件。

注意　gunicorn不能在Windows系统上运行。


安装Heroku CLI后执行书上的命令：heroku login，登陆后报错（不管有没有代理都是）：IP address mismatch

查了资料发现，书上的命令应该换成：heroku login -i，（手机用小飞机并且开代理，之前deepin装飞机失败，暂时这么操作，之后再尝试）使用邮箱名和密码登录，之后heroku create，然后git push heroku master失败报错，是python版本问题

邮箱：eric@example.com
密码：eric123456

# 推送到Heroku
首先，在终端会话中，使用你在https://heroku.com/创建账户时指定的用户名和密码来登录Heroku（见❶）。然后，让Heroku创建一个空项目（见❷）。Heroku生成的项目名由两个单词和一个数字组成，你以后可修改这个名称。接下来，我们执行命令gitpush heroku master（见❸），它让Git将项目的分支master推送到Heroku刚才创建的仓库中；Heroku随后使用这些文件在其服务器上创建项目。❹处列出了用于访问这个项目的URL。执行这些命令后，项目就部署好了，但还未对其做全面的配置。为核实正确地启动了服务器进程，请执行命令heroku ps：
输出指出了在接下来的24小时内，项目还可在多长时间内处于活动状态（见❶）。编写本书时，Heroku允许免费部署在24小时内最多可以有18小时处于活动状态。项目的活动时间超过这个限制后，将显示标准的服务器错误页面，稍后我们将设置这个错误页面。在❷处，我们发现启动了Procfile指定的进程。
现在，我们可以使用命令heroku open在浏览器中打开这个应用程序了：

注意　部署到Heroku的流程会不断变化。如果你遇到无法解决的问题，请通过查看Heroku文档来获取帮助。为此，可访问https://devcenter.heroku.com/，单击Python，再单击链接Getting Started with Django。如果你看不懂这些文档，请参阅附录C提供的建议。
