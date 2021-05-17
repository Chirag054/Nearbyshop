from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from geopy.distance import  great_circle
# Create your views here.

def home(request):
    return render(request , 'home.html')

def api(request):
    shop_objs = Shop.objects.all()
    
    pincode = request.GET.get('pincode')
    km = request.GET.get('km')
    user_lat = None
    user_long = None
    
    if pincode:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(int(pincode))
        user_lat = location.latitude
        user_long = location.longitude 
    
    
    payload = []
    for shop_obj in shop_objs:
        result = {}
        result['name'] = shop_obj.name
        result['description'] = shop_obj.description
        result['pincode'] = shop_obj.pincode
        if pincode:
            first = (float(user_lat) , float(user_long))
            second = (float(shop_obj.lat) , float(shop_obj.lon))
            result['distance'] = int( great_circle(first , second).miles)
        
        payload.append(result)
        
        if km:
            if result['distance'] > int(km):
                payload.pop()
             
    return JsonResponse(payload , safe=False)
    
    
    
    