from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import PizzaDataSerializer
from pizza_app.models import PizzaModel


@api_view(http_method_names=['GET','POST'])
def pizza_data_view(request):
    if request.method == 'GET':
        return pizza_data_view_get(request)
    elif request.method == 'POST':
        return pizza_data_view_post(request)

@api_view(http_method_names=['PUT','DELETE'])
def pizza_data_edit_view(request,id):
    if request.method == 'PUT':
        return pizza_data_view_update(request, id)
    elif request.method == 'DELETE':
        return pizza_data_view_delete(request, id)


def pizza_data_view_get(request):
    pizzaType = request.GET.get('type','') 
    pizzaSize = request.GET.get('size','')
    try:
        if pizzaType == '' and pizzaSize == '':
            data = PizzaModel.objects.all()
        elif not(pizzaType == '' and pizzaSize == ''):
            data = PizzaModel.objects.filter(pizzaSize=pizzaSize, pizzaType=pizzaType)
        serializer = PizzaDataSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def pizza_data_view_post(request):
    data=request.data
    serializer = PizzaDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def pizza_data_view_update(request, id):
    id_data =  PizzaModel.objects.get(pk=id)
    serializer = PizzaDataSerializer(id_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def pizza_data_view_delete(request, id):
    data =  PizzaModel.objects.get(pk=id)
    data.delete()
    return Response("Deleted Successfully")


