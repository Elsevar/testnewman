from pyexpat import model
from rest_framework import serializers

from githubactions.models import Item

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['name', 'description']