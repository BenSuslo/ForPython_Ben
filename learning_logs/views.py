from django.shortcuts import render
from .models import Topic, Entry
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')
# 装饰器（decorator）是放在函数定义前面的指令，Python在函数运行前，根据它来修改函数代码的行为
# login_required()作为装饰器用于视图函数topics()——在它前面加上符号@和login_required，让Python在运行topics()的代码前先运行login_required()的代码。login_required()的代码检查用户是否已登录，仅当用户已登录时，Django才运行topics()的代码。如果用户未登录，就重定向到登录页面。
@login_required
def topics(request):
    """显示所有的主题"""
    # 查询数据库——请求提供Topic对象，并按属性date_added对它们进行排序
    # 用户登录后，request对象将有一个user属性，这个属性存储了有关该用户的信息。代码Topic.objects.filter(owner=request.user)让Django只从数据库中获取owner属性为当前用户的Topic对象
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
@login_required
def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    # date_added前面的减号指定按降序排列，即先显示最近的条目
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
# 处理两种情形：刚进入new_topic网页（在这种情况下，它应显示一个空表单）；对提交的表单数据进行处理，并将用户重定向到网页topics
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            # 调用form.save()，并传递实参commit=False，这是因为我们先修改新主题，再将其保存到数据库中
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # HttpResponseRedirect类，用户提交主题后我们将使用这个类将用户重定向到网页topics
            # 函数reverse()根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成URL
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 实参commit=False，让Django创建一个新的条目对象，并将其存储到new_entry中，但不将它保存到数据库中
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            # 调用save()，且不指定任何实参。这将把条目保存到数据库，并将其与正确的主题相关联
            new_entry.save()
            # 供两个实参：要根据它来生成URL的URL模式的名称；列表args，其中包含要包含在URL中的所有实参。
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        # 使用实参instance=entry创建一个EntryForm实例
        # 这个实参让Django创建一个表单，并使用既有条目对象中的信息填充它。用户将看到既有的数据，并能够编辑它们。
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)