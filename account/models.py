# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Credentials(models.Model):
    credential_name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=40)
    secret_key = models.CharField(max_length=50)
    tenant_id = models.CharField(max_length=40)
    subscription_id = models.CharField(max_length=40)
    bearer_token = models.CharField(max_length=2000, default='0')
    token_expire_on = models.CharField(max_length=15, default='0')
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.credential_name


