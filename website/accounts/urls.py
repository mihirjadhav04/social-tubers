# from django.contrib import admin
from django.urls import path, include

# from django.conf.urls.static import static

# extra part[import] for static configuration
# from django.conf import settings
# from django.conf.urls.static import static
from .views import (
    InfluencerSignUpView,
    BrandSignUpView,
    Influencers,
    InfluencerDetails,
    Brands,
)

urlpatterns = [
    path(
        "signup/influencer/", InfluencerSignUpView.as_view(), name="influencer_signup"
    ),
    path("signup/brand/", BrandSignUpView.as_view(), name="brand_signup"),
    path("influencers/", Influencers, name="influencers"),
    path("influencer_details/<int:id>/", InfluencerDetails, name="influencer_details"),
    path("brands/", Brands, name="brands"),
]
