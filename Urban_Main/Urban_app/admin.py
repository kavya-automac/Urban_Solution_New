from django.contrib import admin

# Register your models here.

from . models import *

@admin.register(Reports_data)
class Reports_data_Admin(admin.ModelAdmin):
    list_display = ['id','Timestamp','CycleTime','StartTime','StopTime','Input_data','Output_data','Power_Consume']
