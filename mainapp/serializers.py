from  rest_framework import serializers

from mainapp.models import(
     Company,Job,Event,Video,
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id','name','logo', 'description',
            'telegram','whatsapp', 
)


class JobSerializer(serializers.ModelSerializer):
    # school_name = serializers.ReadOnlyField(source='school.name') 
    company = CompanySerializer(read_only=True, many=True)       
    class Meta:
        model = Job
        fields = (
            'id','company','position',
            'salary','type',
)


class EventSerializer(serializers.ModelSerializer):
    job= JobSerializer(read_only=True, many=True)
    class Meta:
        model = Event
        fields = (
            'id', 'name','job','location', 
            'date','website' ,'registration',
            'description','image',
)

class VideotSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=True)
    class Meta:
        model = Video
        fields = (
            'id','name','event',
            'date','image','video',
)
