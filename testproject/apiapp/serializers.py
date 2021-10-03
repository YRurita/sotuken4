from rest_framework import serializers

from .models import GridItem, person_in_the_room, num_of_people
class GridItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridItem
        # 出力したいフィールド名をタプルで(括弧とカンマ)で定義します。
        fields = ('number', 'name', 'picture')

class person_in_the_roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = person_in_the_room
        fields = ('number', 'name')

class num_of_peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = num_of_people
        fields = ('num',)


