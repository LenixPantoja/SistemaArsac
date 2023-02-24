from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .serializers import PersonasSerializers, UsuariosSerializers
from .models import Persona
from django.contrib.auth.models import User


# Create your views here.

class PersonaApiView(APIView):
    
    def post(self, request, format = None):
        serializer = UsuariosSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format = None, *args, **kwargs):
        usuarios = User.objects.all()

        serializer = UsuariosSerializers(usuarios, many=True)
        return Response(serializer.data)


# PUT DELETE