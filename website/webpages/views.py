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


# def service(request):
#     return render(request, "webpages/service.html")


def searchresultpage(request):
    return render(request, "webpages/search.html")
