from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from account.models import Images, User
from .serializers import ImagesSerializer
from rest_framework.response import Response
from rest_framework import status


class ImagesViewSet(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
