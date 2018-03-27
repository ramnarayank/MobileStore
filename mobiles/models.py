# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Devices(models.Model):
    device_name = models.CharField(max_length=200)
    device_model = models.CharField(max_length=100)


    def __str__(self):
        return self.device_name+ "-"+ self.device_model

    def get_absolute_url(self):
        return reverse('mobiles:index')


class DeviceDetails(models.Model):
    devices = models.ForeignKey(Devices, on_delete=models.CASCADE)
    device_price = models.CharField(max_length=200)
    device_memory = models.CharField(max_length=200)
    def __str__(self):
        return self.devices.device_name+"-"+self.devices.device_model+"-"+self.device_price