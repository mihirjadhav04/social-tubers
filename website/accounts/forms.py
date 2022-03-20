from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import User, Influencer, Brand


class InfluencerSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Choose your password.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm your password.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your first name.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    youtube_id = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter you youtube channel id.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    channel_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter you youtube channel name.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    instagram_id = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your instagram id.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    category_type = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your category",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    short_description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Describe yourself in short.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    profile_photo = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "placeholder": "Select your profile photo.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )

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
        influencer.channel_name = self.cleaned_data.get("channel_name")
        influencer.youtube_id = self.cleaned_data.get("youtube_id")
        influencer.instagram_id = self.cleaned_data.get("instagram_id")
        influencer.category_type = self.cleaned_data.get("category_type")
        influencer.short_description = self.cleaned_data.get("short_description")
        influencer.profile_photo = self.cleaned_data.get("profile_photo")
        influencer.save()
        return influencer


class BrandSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Choose your password.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm your password.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your first name.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )

    brand_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter you youtube brand name.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    instagram_id = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your instagram id.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    category_type = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your category",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    short_description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Describe yourself in short.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    profile_photo = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "placeholder": "Select your profile photo.",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    established_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "When your brand started? - dd/mm/yyyy",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )

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


class CommonSignInForm(forms.Form):
    pass
