from rest_framework import  serializers
from .models import *




class LaptopsSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = "__all__"

