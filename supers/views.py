from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SuperSerializer
from .models import Super





@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        heros = Super.objects.all()
        serializer = SuperSerializer(supply, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['GET','PUT','DELETE'])
def supers_detail(request, pk):

    sup_er = get_list_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(sup_er)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = SuperSerializer(sup_er, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        sup_er.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    




