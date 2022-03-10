from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from githubactions.models import Item
from githubactions.serializers import ItemSerializer

# Create your views here.

class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        item_serializer = ItemSerializer(instance=items, many=True)
        return Response(data=item_serializer.data)
        
    def post(self, request):
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(data=item_serializer.data, status=status.HTTP_200_OK)
        return Response(data=item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

