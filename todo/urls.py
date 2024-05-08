from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('list',views.listd),
    path('add/',views.add_task),
    path('todo',ListTodoAPIView.as_view(),name='todo'),
    path('detail/<str:pk>/',detailesTodoAPIView.as_view(),name='detail'),
    path('create/',createTodoAPIView.as_view(),name='create'),
    path('update/<str:pk>/',updateTodoAPIView.as_view(),name='update'),
    path('delete/<str:pk>/',deleteTodoAPIView.as_view(),name='delete'),
    ]