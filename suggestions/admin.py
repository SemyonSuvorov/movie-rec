from django.contrib import admin
from .models import Suggestion


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ["content_object", "user", "value", 'timestamp']
    raw_id_fields = ["user"]
    readonly_fields = ["content_object", 'timestamp']
    search_fields = ["user__username"]


admin.site.register(Suggestion, SuggestionAdmin)

