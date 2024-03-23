from django.contrib import admin
from .models import Export


class ExportAdmin(admin.ModelAdmin):
    list_display = ['type', 'timestamp', 'latest']
    list_filter = ['latest', 'type', 'timestamp', ]


admin.site.register(Export, ExportAdmin)
