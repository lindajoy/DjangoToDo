from rest_framework import serializers
from lists import  models

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'Title',
            'Description',
            'completed',
        )

        model = models.list