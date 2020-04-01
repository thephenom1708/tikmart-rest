from django.contrib import admin

from lucky_draw.models import LuckyDraw, LuckyDrawProfile


class LuckyDrawProfile(admin.TabularInline):
    model = LuckyDrawProfile
    extra = 0
    verbose_name = "Lucky Draw User Profile"
    verbose_name_plural = "Lucky Draw User Profiles"


class LuckyDrawAdmin(admin.ModelAdmin):
    inlines = [LuckyDrawProfile]
    list_display = ['id', 'created_on', 'finished_on', 'winner', 'order_amount_limit', 'active']
    list_filter = ['created_on', 'active']
    search_fields = ['winner__email', 'winner__first_name', 'winner__last_name', 'users__first_name', 'users__email']
    ordering = ['created_on']


admin.site.register(LuckyDraw, LuckyDrawAdmin)
