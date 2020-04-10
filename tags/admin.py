from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'usage_count']
    list_filter = ['type']
    search_fields = ['title', 'type']

    def usage_count(self, obj):
        return obj.products.all().count()

    usage_count.short_description = "Usage Count"


admin.site.register(Tag, TagAdmin)
