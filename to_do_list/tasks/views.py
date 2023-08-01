from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TagForm, TaskForm
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


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")


class CompleteTaskView(View):

    def post(self, request, *args, **kwargs):
        task_id = self.kwargs["pk"]
        task = get_object_or_404(Task, id=task_id)
        task.performance = True
        task.save()

        return HttpResponseRedirect(reverse_lazy("tasks:task_list"))


class CancelTaskView(View):

    def post(self, request, *args, **kwargs):
        task_id = self.kwargs["pk"]
        task = get_object_or_404(Task, id=task_id)
        task.performance = False
        task.save()

        return HttpResponseRedirect(reverse_lazy("tasks:task_list"))


