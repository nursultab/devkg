from  rest_framework import serializers

from mainapp.models import(
     Company,Job,Event,Video,
)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
          'id','name','event',
          'date','image','video',  
)

class EventSerializer(serializers.ModelSerializer):
    videos= VideoSerializer(read_only=True, many=True)
    class Meta:
        model = Event
        fields = (
            'id', 'name','job','location', 
            'date','website' ,'registration',
            'description','image','videos',
)

class JobSerializer(serializers.ModelSerializer):
    events = EventSerializer(read_only=True, many=True)       
    class Meta:
        model = Job
        fields = (
            'id','company','position',
            'salary','type','events',
)

class CompanySerializer(serializers.ModelSerializer):
    jobs = JobSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = (
            'id','name','logo', 'description',
            'telegram','whatsapp','jobs',
)






