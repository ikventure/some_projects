from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # 根据Topic模型创建表单
        fields = ['text'] # 只包含字段text
        labels = {'text': ''} # 不生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 定义text字段的widgets小部件，将文本区域的宽度设置为80列
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

