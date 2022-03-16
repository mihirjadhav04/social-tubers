from django.contrib import admin
from django.urls import path, include

# from django.conf.urls.static import static
from .views import influencers, influencer_details

urlpatterns = [
    path("influencers/", influencers, name="influencers"),
    # path("<int:id>", influencer_details, name="influencer_details"),
    path("influencer_details/<int:id>/", influencer_details, name="influencer_details"),
]
