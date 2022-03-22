from django.shortcuts import render
from accounts.models import Influencer

# Create your views here.
def homepage(request):
    featured_youtubers = Influencer.objects.order_by("-created_date").filter(
        is_featured=True
    )
    # tuber = get_object_or_404(Youtuber, pk=id)
    # recent_tubers = Youtuber.objects.order_by("-created_date")
    data = {
        "featured_youtubers": featured_youtubers,
        # "recent_tubers": recent_tubers,
    }
    return render(request, "webpages/homepage.html", data)


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
