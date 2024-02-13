from django.shortcuts import render
from .models import Items
from .serializers import ItemSerializer
from rest_framework.generics import ListAPIView
from rest_framework import permissions
# Create your views here.
class ItemView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.AllowAny,)