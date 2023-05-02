from rest_framework.viewsets import ModelViewSet

from mainapp.models import (
    Company,Job,Event,Video,
)

from mainapp.serializers import(
    CompanySerializer,
)

class CompanyView(ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


from mainapp.serializers import(
    JobSerializer,
)

class JobView(ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer




from mainapp.serializers import(
    EventSerializer,
)

class EventView(ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

from mainapp.serializers import(
    VideotSerializer,
)

class VideoView(ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideotSerializer