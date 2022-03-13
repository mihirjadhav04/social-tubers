from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("aboutpage/", views.aboutpage, name="aboutpage"),
    path("contactpage/", views.contactpage, name="contactpage"),
    path("service/", views.service, name="service"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    # path("influencers/", views.influencers, name="influencers"),
]
