#Saimon pass:Saimon0168
from django.contrib import admin
from .models import OnGoingProject
from .models import UpcomingProject, CompletedProject, Home

admin.site.register(OnGoingProject)
admin.site.register(UpcomingProject)
admin.site.register(CompletedProject)
admin.site.register(Home)