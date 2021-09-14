from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题和它的条目"""
    topic = get_object_or_404(Topic, id=topic_id)
    # 确保主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    # 添加新主题
    if request.method != 'POST':
        # 刚进入new_topic页面，GET方法，未提交数据，则创建一个空表单
        form = TopicForm()
    else:
        # POST提交了数据，对表单数据进行处理，并将用户重定向到topics页面
        form = TopicForm(data=request.POST)
        # 检查表单是否有效
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # 不是POST请求，显示空表单或无效表单
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    # 为特定主题添加新条目
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        # 判断数据是否有效
        if form.is_valid():
            # 创建一个新的条目对象，并把它赋值给new_entry，需要添加topic属性，所以commit=False表示不提交
            new_entry = form.save(commit=False)
            # 设置对应主题
            new_entry.topic = topic
            # 存入数据库
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    # 编辑已经存在的条目
    # 根据entry_id获取entry和相应topic
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # 确保条目对应主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST请求，根据既有条目对象创建一个表单实例，并根据request.POST对它进行修改
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # 表单有效，则保存
            form.save()
            # 重定向到该主题页面
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
