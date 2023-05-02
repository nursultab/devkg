from django.contrib import admin


from mainapp.models import Company,Job,Event,Video

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Event)
admin.site.register(Video)