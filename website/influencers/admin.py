from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Youtuber


class Youtuber_AdminPanelView(admin.ModelAdmin):
    # method to modify the fields or it's view in the Admin Panel
    def myphoto(self, object):
        # format_html allows you to format specific features of the fields
        return format_html('<img src={} width="40" />'.format(object.profile_photo.url))

    list_display = ("id", "myphoto", "influencer_name", "is_featured")
    search_fields = ("influencer_name",)
    list_filter = ("category",)
    list_display_links = ("id", "influencer_name")

    # to make you field editable
    list_editable = ("is_featured",)


admin.site.register(Youtuber, Youtuber_AdminPanelView)
