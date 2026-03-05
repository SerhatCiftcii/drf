from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import serializers
from products.models import Product
from product.serializers import Por
@api_view(['GET'])
def api_views(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id","title","price","sale_price"])
    return Response(data)