from rest_framework.renderers import JSONRenderer

from playground.models import Animal
from playground.serializers import AnimalSerializer

animal = Animal(name='Jaguar', color='yellow', sex='male')
animalSerializer = AnimalSerializer(animal)
json = JSONRenderer().render(animalSerializer.data)
data = animalSerializer.data
print(f'Animal serialized: {data} JSONd: {json} ToRep: {animalSerializer.to_representation(animal)}')

animalSerializer = AnimalSerializer(data=data)
animalSerializer.is_valid()
print(f'Deserializing. Validated data: {animalSerializer.validated_data} InternalValue: {animalSerializer.to_internal_value(data)}')

dataList = [
    {'name': 'Lion', 'color': 'Yellow', 'sex': 'female'},
    {'name': 'Tiger', 'color': 'White', 'sex': 'female'},
    {'name': 'Bear', 'color': 'Brown', 'sex': 'male'}]
animalSerializer = AnimalSerializer(data=dataList, many=True)
animalSerializer.is_valid()
animalObjs = animalSerializer.save()
print(f'Created multiple animals: {animalObjs}')