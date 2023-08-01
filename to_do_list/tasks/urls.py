from django.urls import path

from tasks.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CompleteTaskView,
    CancelTaskView
)

app_name = "tasks"

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task_list"
        ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list"
        ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag_create"
        ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag_update"
        ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag_delete"
        ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task_create"
        ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update"
        ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete"
        ),
    path(
        "task/complete/<int:pk>/",
        CompleteTaskView.as_view(),
        name="complete_task"
        ),
    path(
        "task/cancel/<int:pk>/",
        CancelTaskView.as_view(),
        name="cancel_task"
        ),
]
