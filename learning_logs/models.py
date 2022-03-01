from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 模型告诉Django如何处理应用程序中存储的数据。
# 在代码层面，模型就是一个类，就像前面讨论的每个类一样，包含属性和方法。
# 注意　要获悉可在模型中使用的各种字段，请参阅DjangoModel Field Reference（Django模型字段参考），其网址为https://docs.djangoproject.com/en/1.8/ref/models/fields/。就当前而言，你无需全面了解其中的所有内容，但自己开发应用程序时，这些内容会提供极大的帮助。
# Model——Django中一个定义了模型基本功能的类
class Topic(models.Model):
    """用户学习的主题"""
    # 属性text是一个CharField——由字符或文本组成的数据
    # 定义CharField属性时，必须告诉Django该在数据库中预留多少空间
    # max_length设置成了200（即200个字符）
    text = models.CharField(max_length=200)
    # 属性date_added是一个DateTimeField——记录日期和时间的数据
    # 实参auto_now_add=True，每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    # 我们需要告诉Django，默认应使用哪个属性来显示有关主题的信息。Django调用方法__str__()来显示模型的简单表示。
    # 注意　如果你使用的是Python 2.7，应调用方法__unicode__()，而不是__str__()，但其中的代码相同。
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # DJANGO从1.9开始FOREIGNKEY中的ON_DELETE参数是必须的。
    # TYPEERROR: __INIT__() MISSING 1 REQUIRED POSITIONAL ARGUMENT: 'ON_DELETE'
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # TextField实例不需要长度限制
    text = models.TextField()
    # 属性date_added让我们能够按创建顺序呈现条目，并在每个条目旁边放置时间戳
    date_added = models.DateTimeField(auto_now_add=True)
    # 嵌套Meta类，Meta存储用于管理模型的额外信息
    class Meta:
        # 设置一个特殊属性，让Django在需要时使用Entries来表示多个条目
        # 如果没有这个类，Django将使用Entrys来表示多个条目
        verbose_name_plural = 'entries'
    # 方法__str__()告诉Django，呈现条目时应显示哪些信息
    # 让Django只显示text的前50个字符
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+"..."