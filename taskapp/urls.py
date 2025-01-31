from django.urls import path
from . import views

app_name = 'taskapp'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('like-detail/<int:post_id>/',
        views.like_toggle,
        name='like_detail'),
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),
    path(
        'task-detail/<int:pk>/',
        views.TaskDetail.as_view(),
        name= 'task_detail'
    ),
    path(
        'science-list/',
        views.ScienceView.as_view(),
        name = 'science_list'
    ),
    path(
        'sports-list/',
        views.SportsView.as_view(),
        name = 'sports_list'
    ),
    path(
        'IT-list/',
        views.ITView.as_view(),
        name = 'IT_list'
    ),
    path(
        'international-list/',
        views.InternationalView.as_view(),
        name = 'international_list'
    ),
    path(
        'entertainment-list/',
        views.EntertainmentView.as_view(),
        name = 'entertainment_list'
    ),
    path(
        'economy-list/',
        views.EconomyView.as_view(),
        name = 'economy_list'
    ),
    path(
        'domestic-list/',
        views.DomesticView.as_view(),
        name = 'domestic_list'
    ),
    
]