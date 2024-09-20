from .models import *
from rest_framework import serializers


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports_data
        fields = ["Timestamp","CycleTime","StartTime","StopTime","Input_data","Output_data","Power_Consume"]
