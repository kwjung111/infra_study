from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.parsers import JSONParser
from order.serializers import ShopSerializer,MenuSerializer,OrderFoodSerializer,OrderSerializer
from order.models import Shop,Menu,Order,OrderFood


@csrf_exempt
def shop(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        return render(request, 'order/shop_lists.html', {'shop_list' : shop})
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def menu(request, shop):
    if request.method == 'GET':
        menu = Menu.objects.filter(shop=shop)
        return render(request, 'order/menu_lists.html', {'menu_list' : menu, 'shop' : shop})
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def order(request):
    if request.method == 'POST':
        address = request.POST['address']
        shop    = request.POST['shop']
        food_list =  request.POST.getlist('menu')
        order_date = timezone.now()
        
        shop_item = Shop.objects.get(pk=shop)
        
        shop_item.order_set.create(address= address,order_date = order_date,shop=int(shop))
        order_item = Order.objects.get(pk = shop_item.order_set.latest('id').id)
        for food in food_list :
            order_item.orderfood_set.create(food_name=food)
        
        return render(request, 'order/success.html')
    
    elif request.method =='GET':
        order_list = Order.objects.all()
        return render(request, 'order/order_lists.html', {'order_list' : order_list})