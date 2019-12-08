from rest_framework import serializers
from .models import ItemsModel,UserModel,Catagory


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        # fields = ('product_id', 'name','price','about','quantity')
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # fields = ('user_id', 'user_name','password','name','address','pin','mobile_number','state')
        fields = '__all__'
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'
