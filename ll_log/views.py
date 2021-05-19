from django.shortcuts import render
from .models import Entry, Topic 

# Create your views here.

def index(request):
    """The learning log home page"""
    return render(request, 'll_log/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'll_log/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by()
    context = {'topic': topic, 'entries': entries}
    return render(request, 'll_log/topic.html', context) 