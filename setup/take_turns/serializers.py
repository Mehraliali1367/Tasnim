from rest_framework import serializers
from .models import Doctor, Presence, Visit


class DoctorSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.serial")

    class Meta:
        model = Doctor
        fields = "__all__"


class PresenceSerializer(serializers.ModelSerializer):
    def get_more_doctor(self, obj):
        return {
            "name": obj.doctor.name,
            "id": obj.doctor.id
        }

    doctor = serializers.SerializerMethodField("get_more_doctor")

    class Meta:
        model = Presence
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("hour", "datetime_persian")
