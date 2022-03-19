from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "webpages/homepage.html")


def aboutpage(request):
    return render(request, "webpages/aboutpage.html")


def contactpage(request):
    return render(request, "webpages/contactpage.html")


def service(request):
    return render(request, "webpages/service.html")


def login(request):
    return render(request, "webpages/login.html")


def signup(request):
    return render(request, "webpages/signup.html")


def influencer_signup(request):
    return render(request, "webpages/influencer-signup.html")


def brand_signup(request):
    return render(request, "webpages/brand_signup.html")


# def influencer_details(request):
#     return render(request, "webpages/influencer_details.html")

# def influencers(request):
#     return render(request, "webpages/influencers.html")
