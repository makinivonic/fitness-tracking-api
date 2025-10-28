from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username",read_only=True)

    class Meta:
        model = Activity
        fields = ['username', 'activity_type', 'duration', 'distance', 'calories_burnt', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']