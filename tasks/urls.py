from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_list', views.getIndexList),
    path('index_post', views.postIndexList),
    path('index_delete', views.deleteIndexList)
]
