from django.urls import path
from . import views 

urlpatterns=[
    # path('',views.index,name='index'),
    path('tweet/',views.list_tweets,name='tweet_list'),
    path('create/',views.create_tweet,name='create_tweet'),
    path('<int:pk>/edit/',views.edit_tweet,name='edit_tweet'),
    path('<int:pk>/delete/',views.delete_tweet,name='delete_tweet'),
    path('register/',views.register, name='register'),
]