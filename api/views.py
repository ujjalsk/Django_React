from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.models import ItemsModel,UserModel,Catagory
from .serielizers import ItemsSerializer,UserSerializer,CatagorySerializer


class ItemsListView(ListAPIView):
    queryset = ItemsModel.objects.all()
    serializer_class = ItemsSerializer


class ItemsDetailView(RetrieveAPIView):
    queryset = ItemsModel.objects.all()
    serializer_class = ItemsSerializer

class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class CatagoryListView(ListAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer


class CatagoryDetailView(RetrieveAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

# class CatagoryItemsDetailView(RetrieveAPIView):
#     queryset = Catagory.objects.all()
#     serializer_class = CatagorySerializer


def index(response):
    return render(response,"api/base.html")