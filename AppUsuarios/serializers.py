from rest_framework import serializers
from .models import Persona
from django.contrib.auth.models import User

class PersonasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        
class UsuariosSerializers(serializers.ModelSerializer):
    persona = PersonasSerializers()

    class Meta:
        model = User
        fields = '__all__'
        
