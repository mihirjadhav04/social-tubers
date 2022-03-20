from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import User, Influencer, Brand


class InfluencerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    youtube_id = forms.CharField(required=True)
    instagram_id = forms.CharField(required=True)
    category_type = forms.CharField(required=True)
    short_description = forms.CharField(required=True)
    profile_photo = forms.ImageField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ("username",)

    def save(self):
        user = super().save(commit=False)
        user.is_influencer = True
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        influencer = Influencer.objects.create(user=user)
        influencer.youtube_id = self.cleaned_data.get("youtube_id")
        influencer.instagram_id = self.cleaned_data.get("instagram_id")
        influencer.category_type = self.cleaned_data.get("category_type")
        influencer.short_description = self.cleaned_data.get("short_description")
        influencer.profile_photo = self.cleaned_data.get("profile_photo")
        influencer.save()
        return influencer


class BrandSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    brand_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    instagram_id = forms.CharField(required=True)
    category_type = forms.CharField(required=True)
    short_description = forms.CharField(required=True)
    profile_photo = forms.ImageField(required=True)
    established_date = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ("username",)

    def save(self):
        user = super().save(commit=False)
        user.is_influencer = True
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        brand = Brand.objects.create(user=user)
        brand.brand_name = self.cleaned_data.get("instagram_id")
        brand.instagram_id = self.cleaned_data.get("instagram_id")
        brand.category_type = self.cleaned_data.get("category_type")
        brand.short_description = self.cleaned_data.get("short_description")
        brand.profile_photo = self.cleaned_data.get("profile_photo")
        brand.save()
        return brand
