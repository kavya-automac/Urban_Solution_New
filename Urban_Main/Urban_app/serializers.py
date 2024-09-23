from .models import *
from rest_framework import serializers


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports_data
        fields = ["Timestamp","CycleTime","StartTime","StopTime","Input_data","Output_data","Power_Consume"]
class CummulativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cummulative_report_data
        fields = ["date_data","Cycle_No","Cycle_start_timestamp","Cycle_complete_timestamp","waste_add","power_consumed","compost_removed"]