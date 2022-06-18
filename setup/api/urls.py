from django.urls import path, include
from . import views

# from rest_framework import routers

app_name = "api"

# router = routers.SimpleRouter()
# router.register('', views.ImagesViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    path('t/', views.ImagesViewSet.as_view()),

]
