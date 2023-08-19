from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "auction", "price", "created_date","created_update", "created_image"]
    list_filter = ["auction", "created_at"]
    search_fields = ["title"]
    actions = ["mark_auction_as_true", "mark_auction_as_false"]

    fieldsets=(
        ('Общая информация',{
           "fields": ("title","description","user", "image"),
           "classes":["collapse"]
        }),
        ('Финансы',{
           "fields": ("price","auction"),
           "classes":["collapse"]           
        }),        
    )


    @admin.action(description="Добавить возможность торга")
    def mark_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description="Убрать возможность торга")
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    




# admin.site.register(Advertisement, AdvertisementAdmin)
