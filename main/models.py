from django.db import models

class Day(models.Model):
    week = models.CharField(max_length=200, blank=True, null=True)
    day = models.CharField(max_length=200, blank=True, null=True)
    remain_seat = models.IntegerField(blank=True, null=True)

class Month(models.Model):
    month = models.CharField(max_length=200, blank=True, null=True)
    f_day = models.ForeignKey(Day, related_name='f_day', on_delete=models.CASCADE, blank=True, null=True)