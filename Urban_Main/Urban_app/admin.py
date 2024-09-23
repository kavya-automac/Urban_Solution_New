from django.contrib import admin

# Register your models here.

from . models import *

@admin.register(Reports_data)
class Reports_data_Admin(admin.ModelAdmin):
    list_display = ['id','Timestamp','CycleTime','StartTime','StopTime','Input_data','Output_data','Power_Consume']
@admin.register(Cummulative_report_data)
class Cummulative_data_Admin(admin.ModelAdmin):
    list_display = ['id','date_data','Cycle_No','Cycle_start_timestamp','Cycle_complete_timestamp','waste_add','power_consumed','compost_removed']
