# 让用户输入并提交信息的页面都是表单，哪怕它看起来不像表单。用户输入信息时，我们需要进行验证，确认提供的信息是正确的数据类型，且不是恶意的信息，如中断服务器的代码。然后，我们再对这些有效信息进行处理，并将其保存到数据库的合适地方。这些工作很多都是由Django自动完成的。
from django import forms
from .models import Topic, Entry
class TopicForm(forms.ModelForm):
    # Meta类告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
    class Meta:
        model = Topic
        fields = ['text']
        # 此处代码让Django不要为字段text生成标签
        labels = {'text': ''}
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 小部件（widget）是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。通过设置属性widgets，可覆盖Django选择的默认小部件。
        # 通过让Django使用forms.Textarea，我们定制了字段'text'的输入小部件，将文本区域的宽度设置为80列，而不是默认的40列。
        widgets = {'text': forms.Textarea(attrs={'cols':80})}