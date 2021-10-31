from rest_framework import serializers
from .models import Advisor, Booking, User

class AdvisorSerializer(serializers.ModelSerializer):
    # adID = serializers.AutoField(primary_key=True)
    # adName = serializers.CharField(max_length=20)
    # adPhoto = serializers.CharField(max_length=20)

    # def create(self, validated_data):
    #     return Advisor.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.adName = validated_data.get('adName', instance.adName)
    #     instance.adPhoto = validated_data.get('adPhoto', instance.adName)
    #     instance.save()
    #     return instance
    class Meta:
        model = Advisor
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"