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


