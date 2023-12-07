from rest_framework import generics, mixins, status
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from .permissions import Permissions
from .models import *
from .serializers import LaptopsSerialaizer
from rest_framework.pagination import PageNumberPagination


class LaptopPagination(PageNumberPagination):
    page_size = 1


class LaptopsAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Laptops.objects.all()
    serializer_class = LaptopsSerialaizer
    permission_classes = [Permissions]
    pagination_class = LaptopPagination

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LaptopsAPIDestroy(generics.UpdateAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Laptops.objects.all()
    serializer_class = LaptopsSerialaizer
    permission_classes = [Permissions]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)









