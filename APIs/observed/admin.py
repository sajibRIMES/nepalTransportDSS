from django.contrib import admin
from climatology.models import Absoluteprovertymapbd
from .models import StationInfo

# class RemoteTable1Admin(admin.ModelAdmin):
 
#     list_display = ('objectid', 'dist_name', 'dist_name_old', 'station_name')
#     list_display_links = None
#     search_fields = ['dist_name', 'dist_name_old', 'station_name']
 
#     actions = None
#     enable_change_view = False
 
#     def has_add_permission(self, request):
#         return False
 
#     def has_change_permission(self, request):
#         return False
 
#     def has_delete_permission(self, request, obj=None):
#         return False


admin.site.register(StationInfo)
admin.site.register(Absoluteprovertymapbd)

# Register your models here.
