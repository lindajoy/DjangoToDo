from rest_framework import serializers
from lists import  models

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'Title',
            'Description',
        )

        model = models.list