from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name="create_task"),
    path('<int:pk>/', views.TaskRetrieveDestroyView.as_view(), name="rd_task"),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name="update_task"),
    path('user/<int:pk>/', views.UserTasksView.as_view(), name="user_tasks"),
    path('search_task/', views.SearchListView.as_view(), name="task_search"),
]
# сделать поиск