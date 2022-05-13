from django.contrib import admin

# # Register your models here.
from .models import User, Influencer, Brand

from django.utils.html import format_html

class UserAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    

class Influencer_AdminPanelView(admin.ModelAdmin):
    # method to modify the fields or it's view in the Admin Panel
    def myphoto(self, object):
        # format_html allows you to format specific features of the fields
        return format_html('<img src={} width="50" />'.format(object.profile_photo.url))

    list_display = (
        # "id",
        "myphoto",
        "channel_name",
        "category_type",
        "is_featured",
    )
    search_fields = ("channel_name",)
    list_filter = ("category_type",)
    list_display_links = (
        "myphoto",
        "channel_name",
        "category_type",
    )

    # to make you field editable
    list_editable = ("is_featured",)


class Brand_AdminPanelView(admin.ModelAdmin):
    # method to modify the fields or it's view in the Admin Panel
    def myphoto(self, object):
        # format_html allows you to format specific features of the fields
        return format_html('<img src={} width="50" />'.format(object.profile_photo.url))

    list_display = (
        # "id",
        "myphoto",
        "brand_name",
        "category_type",
        "is_featured",
    )
    search_fields = ("brand_name",)
    list_filter = ("category_type",)
    list_display_links = (
        "myphoto",
        "brand_name",
        "category_type",
    )

    # to make you field editable
    list_editable = ("is_featured",)


admin.site.register(Influencer, Influencer_AdminPanelView)
# admin.site.register(Influencer)
admin.site.register(User,UserAdmin)
admin.site.register(Brand, Brand_AdminPanelView)
