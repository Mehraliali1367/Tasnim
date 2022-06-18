from rest_framework import serializers
from account.models import Images


class ImagesSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.serial")

    class Meta:
        model = Images
        fields = "__all__"
