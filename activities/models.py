from django.db import models
from django.contrib.auth import get_user_model

User  = get_user_model()
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    distance = models.FloatField()
    calories_burnt = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity_type

    class Meta:
        verbose_name_plural = "activities"