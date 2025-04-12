from django.shortcuts import render,redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
import json
from .mongo import collection,database,chocolates_data

collection2 = database['cart']

# Create your views here.
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def login(request):
    return Response({}, template_name = 'login.html')


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def product_list(request):
    if collection.count_documents({}) == 0:
        collection.insert_many(chocolates_data)
    chocolates_list = list(collection.find({}))
    return Response({"chocolates_list" : chocolates_list}, template_name = 'product_list.html')


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def cart(request):
    cart_items = list(collection2.find({}))
    price = sum(float(item['price']) for item in cart_items)
    gst_amount = 0.18 * price
    total_price = price + gst_amount
    return Response({"cart_items" : cart_items, "total_price" : total_price}, template_name = 'cart.html')


@api_view(['POST'])
def handle_login(request):
    if request.method == 'POST':
        email = request.data.get("email")
        password = request.data.get("password")
        with open('data.json', 'r') as file:
            data = json.load(file)
        for item in data:
            if item['email'] == email and item['password'] == password:
                return redirect("/chocolates/product-list/")
            else:
                return redirect("/chocolates/login/")
    return Response("Success", 200)


@api_view(['POST'])
def handle_product_list(request):
    name = request.POST.get('name')
    image = request.POST.get('image')
    price = float(request.POST.get('price'))
    rating = float(request.POST.get('rating'))
    time = request.POST.get('time')

    collection2.insert_one({
        "name": name,
        "image": image,
        "price": price,
        "rating": rating,
        "time": time
    })

    return redirect('/chocolates/cart/')


@api_view(['POST'])
def remove_from_cart(request):
    name = request.data.get("name")
    collection2.delete_one({"name" : name})
    return redirect('/chocolates/cart/')


@api_view(['GET'])
def handle_cart(request):
    return redirect("/chocolates/cart")

