from rest_framework import serializers
from .models import User, MainCycle, Boost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cycle']


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id']


class CycleSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id', 'user', 'coins_count', 'click_power', 'auto_click_power', 'boosts']


class BoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boost
        fields = ['level', 'power', 'price', 'boost_type']
