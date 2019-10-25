from rest_framework import serializers

from events.models import Event

class EventSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=300)
    title = serializers.CharField(max_length=300)
    public = serializers.BooleanField()
    address = serializers.CharField(max_length=300)

    def create(self, validated_data):
        event = Event(**validated_data)
        event.save()
        return event

class EventSerializer2(serializers.Serializer):

    def validate_title(self, value):
        print('Validating title')
        if 'bad' in value:
            raise serializers.ValidationError('Cant have bad word in title')
        return value

    def create(self, validated_data):
        event = Event(**validated_data)
        event.save()
        return event
