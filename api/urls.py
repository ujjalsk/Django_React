from django.urls import path
from .views import ItemsDetailView, ItemsListView, UserDetailView, UserListView, CatagoryDetailView, CatagoryListView, index

app_name = 'api'

urlpatterns = [
    path('items/<pk>', ItemsDetailView.as_view()),
    path('items/', ItemsListView.as_view()),
    path('users/<pk>', UserDetailView.as_view()),
    path('users/', UserListView.as_view()),
    # path('catagory/<pk>/all/', CatagoryDetailView.as_view()),
    path('catagory/<pk>', CatagoryDetailView.as_view()),
    path('catagory/', CatagoryListView.as_view()),
    # path('', index, name='index'),
]
