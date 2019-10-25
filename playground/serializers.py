from rest_framework import serializers

from playground.models import Animal

class AnimalListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        animals = [Animal(**item) for item in validated_data]
        print('Not actually saved')
        return animals

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    color = serializers.CharField(max_length=50)
    sex = serializers.CharField(max_length=20)

    class Meta:
        list_serializer_class = AnimalListSerializer

