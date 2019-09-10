from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('C', 'Created'),
    ('P', 'In Process'),
    ('F', 'Finished'),
    ('D', 'Drop or Failed')
)

class Plans(models.Model):
    PlanId = models.IntegerField(primary_key=True,unique=True)
    Planner = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    Description = models.CharField(max_length=500, blank=True)
    CreateDate = models.DateField(auto_now=True)
    # plan to fill with reward id list
    Rewards = models.CharField(max_length=300, blank=True)
    Days = models.IntegerField(default=30)
    Status = models.CharField(max_length=1, default='C', choices=STATUS_CHOICES)

class Rewards(models.Model):
    RewardId = models.IntegerField(primary_key=True)
    Description = models.CharField(max_length=500, blank=True)

class Tasks(models.Model):
    TaskId = models.IntegerField(primary_key=True)
    PlanId = models.ForeignKey(Plans,
                               on_delete=models.CASCADE)
    Step = models.IntegerField(default=0)
    Description = models.CharField(max_length=500, blank=True)

class KeyResults(models.Model):
    ResultId = models.IntegerField(primary_key=True)
    PlanId = models.ForeignKey(Plans,
                               on_delete=models.CASCADE)
    FinishedSteps = models.CharField(max_length=100, blank=True)
    CheckInDate= models.DateField(auto_now_add=True)
