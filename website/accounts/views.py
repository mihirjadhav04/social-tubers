from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView

# Create your views here.
from .forms import InfluencerSignUpForm, BrandSignUpForm, CommonSignInForm
from .models import User, Influencer, Brand


class InfluencerSignUpView(CreateView):
    model = User
    form_class = InfluencerSignUpForm
    template_name = "accounts/influencer_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect("aboutpage")


class BrandSignUpView(CreateView):
    model = User
    form_class = BrandSignUpForm
    template_name = "accounts/brand_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect("aboutpage")


class CommonSignInView(CreateView):
    model = User
    form_class = CommonSignInForm
    template_name = "accounts/common_signin.html"
