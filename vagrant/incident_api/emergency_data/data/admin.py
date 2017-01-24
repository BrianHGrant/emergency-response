from django.contrib import admin
from data.models import Incident, Agency, Alarmlevel, Censustract, Fireblock

# Register your models here.
admin.site.register(Incident)
admin.site.register(Agency)
admin.site.register(Alarmlevel)
admin.site.register(Censustract)
admin.site.register(Fireblock)
