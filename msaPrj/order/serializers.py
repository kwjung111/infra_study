from rest_framework import serializers
from order.models import Shop,Order,Menu,OrderFood

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'