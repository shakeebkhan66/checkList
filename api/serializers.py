from rest_framework import serializers
from api.models import MyCheckList, MyCheckListItem


class ChecklistItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCheckListItem
        fields = '__all__'


class ChecklistSerializer(serializers.ModelSerializer):
    items = ChecklistItemsSerializer(source='mychecklistitem_set', many=True, read_only=True)

    class Meta:
        model = MyCheckList
        fields = '__all__'
