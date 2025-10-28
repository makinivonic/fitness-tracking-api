from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwner

class ActivitiesView(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Activity.objects.all()

    # def get_queryset(self):
    #     return Activity.objects.filter(user=self.request.user)
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)