from rest_framework import serializers
from base.models import Condominio

class CondominiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'