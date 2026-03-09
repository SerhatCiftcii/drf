from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET'])
def api_views(request,*args,**kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
    #     data = model_to_dict(model_data, fields=["id","title","price","sale_price"])
    if instance:
         data=ProductSerializer(instance).data       
    return Response(data)


@api_view(['POST'])
def api_post(request,*args,**kwargs):
    data = request.data
    # if model_data:
    #     data = model_to_dict(model_data, fields=["id","title","price","sale_price"])
       
    return Response(data)