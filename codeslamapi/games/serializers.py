from rest_framework import serializers
from games.models import Game
from games.models import MyModel


class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    game_category = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('played', instance.played)
        instance.save()
        return instance

class DataSerializer(serializers.Serializer):
    index = serializers.IntegerField(read_only=True)
    symbol = serializers.CharField(max_length=20)
    Date = serializers.DateField()
    Open = serializers.IntegerField()
    High = serializers.IntegerField()
    Low = serializers.IntegerField()
    Close = serializers.IntegerField()
    Volume = serializers.IntegerField()
    AdjustmentFactor = serializers.IntegerField()
    AdjustmentType = serializers.IntegerField()
    avgvolume = serializers.IntegerField()
    
    def create(self, validated_data):
        return MyModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.index = validated_data.get('index', instance.index)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.Date = validated_data.get('Date', instance.Date)
        instance.Open = validated_data.get('Open', instance.Open)
        instance.High= validated_data.get('High',instance.High)
        instance.Low=validated_data.get('Low',instance.Low)
        instance.Close=validated_data.get('Close',instance.Close)
        instance.Volume=validated_data.get('Volume',instance.Volume)
        instance.AdjustmentFactor=validated_data.get('AdjustmentFactor',instance.AdjustmentFactor)
        instance.AdjustmentType=validated_data.get('AdjustmentType',instance.AdjustmentType)
        instance.avgvolume=validated_data.get('avgvolume',instance.avgvolume)
        instance.save()
        return instance



















