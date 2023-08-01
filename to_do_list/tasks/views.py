from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5