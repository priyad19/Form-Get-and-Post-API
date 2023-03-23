from django.contrib import admin
from .models import child,manual,Auto_data
# Register your models here.
@admin.register(child)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(manual)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(Auto_data)
class DataAdmin(admin.ModelAdmin):
    pass
