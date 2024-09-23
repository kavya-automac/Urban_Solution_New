from django.db import models

# Create your models here.

class Reports_data(models.Model):
    objects = models.Manager()
    Timestamp =  models.DateTimeField()
    CycleTime = models.TimeField()
    StartTime = models.TimeField()
    StopTime = models.TimeField()
    Input_data = models.FloatField()
    Output_data = models.FloatField()
    Power_Consume = models.FloatField()

    def __str__(self):
        return "%s %s %s" % (self.Timestamp, self.CycleTime, self.StartTime)


class Cummulative_report_data(models.Model):
    date_data = models.DateTimeField()
    Cycle_No = models.IntegerField()
    Cycle_start_timestamp = models.DateTimeField()
    Cycle_complete_timestamp = models.DateTimeField()
    waste_add = models.FloatField()
    power_consumed = models.FloatField()
    compost_removed = models.FloatField()

    def __str__(self):
        return "%s %s %s" % (self.date_data, self.Cycle_start_timestamp, self.Cycle_complete_timestamp)