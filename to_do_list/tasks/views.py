from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TagForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag_list")
