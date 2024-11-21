from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Condominio
from .serializers import CondominiosSerializer

@api_view(['GET'])
def getData(request):
    condominions = Condominio.objects.all()
    serializer = CondominiosSerializer(condominions, many=True)
    return Response(serializer.data)