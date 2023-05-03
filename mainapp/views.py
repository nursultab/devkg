from rest_framework.viewsets import ModelViewSet

from mainapp.models import (
    Company,Job,Event,Video,
)

from mainapp.serializers import(
    JobSerializer,
    CompanySerializer, 
    EventSerializer,
    VideoSerializer,

)

class CompanyView(ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


class JobView(ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer



class EventView(ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class VideoView(ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer