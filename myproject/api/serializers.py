from rest_framework import serializers
from pizza_app.models import PizzaModel

class PizzaDataSerializer(serializers.Serializer):
    pizzaType = serializers.CharField(max_length=100)
    pizzaSize = serializers.CharField(max_length=100)
    toppings = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return PizzaModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pizzaType = validated_data.get('pizzaType', instance.pizzaType)
        instance.pizzaSize = validated_data.get('pizzaSize', instance.pizzaSize)
        instance.toppings = validated_data.get('toppings', instance.toppings)
        instance.save()
        return instance