from rest_framework import serializers
from .models import Student


#create 
class CreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    loc  = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.loc  = validated_data.get('loc',instance.loc)
        instance.save()
        return instance


