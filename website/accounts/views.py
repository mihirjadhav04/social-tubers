from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView

# Create your views here.
from .forms import InfluencerSignUpForm, BrandSignUpForm, CommonSignInForm
from .models import User, Influencer, Brand

from django.shortcuts import get_object_or_404, render, redirect
from .youtube_stats import YTstats
import json
import pandas as pd
import matplotlib.pyplot as plt
import math

# Create your views here.
# from .models import Influencer, Brands

# for pagiantion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core.mail import send_mail
from django.db.models import Avg

from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# from .models import ContactInfluencer

# latest api key - gamil: jadhavmihir143
# API_KEY = "AIzaSyAvqYKXBzQPwXNgFCcxVP-egG55DQNhs4w"

# API_KEY = "AIzaSyCGEy4EZ4XinMU1voULK5GmZ5DBDE2OVp0"

API_KEY = "AIzaSyBtH1_rHqJGvaLcR8tE-PR16bldFo82YdE"

# API_KEY = "AIzaSyAFUh6biNVO_DoxdiU2qSotXot1WkAouPg"


def CommonLoginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # this will authenticate the user by checking it into the DB.
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # make the user to be login
            auth.login(request, user)
            messages.success(request, "You are logged In")
            return redirect("homepage")

        else:
            messages.error(request, "Invalid Credentials")
    return render(request, "accounts/common_signin.html")


def user_logout(request):
    logout(request)
    messages.error(request, "You have been logged out!")
    return redirect("homepage")


def Options(request):
    return render(request, "accounts/options.html")


class InfluencerSignUpView(CreateView):
    model = User
    form_class = InfluencerSignUpForm
    template_name = "accounts/influencers/influencer_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        # login(self.request, user)
        return redirect("login_page")


class BrandSignUpView(CreateView):
    model = User
    form_class = BrandSignUpForm
    template_name = "accounts/brands/brand_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        # login(self.request, user)
        return redirect("login_page")


class CommonSignInView(CreateView):
    model = User
    form_class = CommonSignInForm
    template_name = "accounts/common_signin.html"


def Brands(request):
    # print("Function called!")
    all_brands = Brand.objects.order_by("-created_date")
    # print(all_brands)
    paginator = Paginator(all_brands, 3)
    page = request.GET.get("page")
    try:
        brands = paginator.page(page)
    except PageNotAnInteger:
        brands = paginator.page(1)
    except EmptyPage:
        brands = paginator.page(all_brands.num_pages)

    data = {
        "all_brands": brands,
    }
    print(all_brands)
    return render(request, "accounts/brands/brands.html", data)


def BrandDetails(request, id):
    brand = get_object_or_404(Brand, pk=id)
    print(brand)
    return render(
        request,
        "accounts/brands/brand_details.html",
    )


def Influencers(request):
    all_tubers = Influencer.objects.order_by("-created_date")

    paginator = Paginator(all_tubers, 3)
    page = request.GET.get("page")
    try:
        tubers = paginator.page(page)
    except PageNotAnInteger:
        tubers = paginator.page(1)
    except EmptyPage:
        tubers = paginator.page(all_tubers.num_pages)

    data = {
        "all_tubers": tubers,
    }
    return render(request, "accounts/influencers/influencers.html", data)


def InfluencerDetails(request, id):
    tuber = get_object_or_404(Influencer, pk=id)
    # This tuber is not all the tubers information, instead it is the information of the tubers with the id that has been passed.

    # print(tuber.channel_id)
    # Passing Manually : channel_id = "UCSegc_0vxRuyJDw_vKGVPmA"

    # Passing the channel id which we are getting it from the current youtubers id selected for details page.
    channel_id = tuber.youtube_id
    subCount = 0
    viewCount = 0
    videoCount = 0
    # creating object of YTstats as yt
    yt = YTstats(API_KEY, channel_id)
    print(yt)
    channel_stats = yt.get_channel_statistics()
    print(channel_stats)
    for key, value in channel_stats.items():
        print(key, value)
        if key == "subscriberCount":
            subCount = value
        if key == "videoCount":
            videoCount = value
        if key == "viewCount":
            viewCount = value

    subCount = convert_count(subCount)
    viewCount = convert_count(viewCount)
    videoCount = convert_count(videoCount)

    video_stats = yt.get_channel_video_data()
    # print(viewCount)
    # Video Statistics
    # Sort video data according to the view count
    sorted_videos = sorted(
        video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True
    )
    stats = []
    for vid in sorted_videos:
        video_id = vid[0]
        title = vid[1]["title"]
        views = int(vid[1]["viewCount"])
        likes = int(vid[1]["likeCount"])
        # dislikes = int(vid[1]["dislikeCount"])
        comments = vid[1]["commentCount"]
        stats.append(
            [
                video_id,
                title,
                views,
                likes,
                # dislikes,
                comments,
            ]
        )

    # print(stats[0][0])
    top_video = stats[0][0]
    # print(stats)
    avg_views = 0
    avg_likes = 0
    # avg_dislikes = 0

    for st in stats:
        avg_views = avg_views + st[2]
        avg_likes = avg_likes + st[3]
        # avg_dislikes = avg_dislikes + st[4]
    avg_likes = avg_likes / len(stats)
    avg_views = avg_views / len(stats)
    # avg_dislikes = avg_dislikes / len(stats)
    avg_data = [round(avg_views), round(avg_likes)]
    # yt.dump()
    # print(len(stats))
    # if request.method == "POST":
    #     client_name = request.POST.get("name")
    #     influencer_name = request.POST.get("influencer_name")
    #     to_email = request.POST.get("influencer_email")
    #     from_email = request.POST.get("email")
    #     subject = request.POST.get("subject")
    #     message = request.POST.get("message")
    #     # print(client_name,client_email, to_email,message,from_email,subject)

    #     contacted_influencer = ContactInfluencer(
    #         client_name=client_name,
    #         client_email=from_email,
    #         influencer_name=influencer_name,
    #         influencer_email=to_email,
    #         subject=subject,
    #         message=message,
    #     )

    #     contacted_influencer.save()

    #     send_mail(
    #         subject,
    #         message + "\n\n\nFor Further Details,\nContact On: " + from_email,
    #         from_email,
    #         [to_email],
    #     )
    #     # contacted_influencer =
    #     return redirect("home")

    data = {
        "tuber": tuber,
        "avg_data": avg_data,
        "subCount": subCount,
        "viewCount": viewCount,
        "videoCount": videoCount,
        "stats": stats,
        "top_video": top_video,
    }
    return render(request, "accounts/influencers/influencer_details.html", data)


def convert_count(num):

    num_len = len(str(num))
    num_in_int = int(num)
    str_num = 0
    if num_len < 4:
        str_num = num
    elif num_len < 7:
        if num_in_int % 1000 != 0:
            temp = format(num_in_int / 1000, ".1f")
        else:
            temp = int(num_in_int / 1000)

        str_num = str(temp) + "K"
    elif num_len <= 10:
        if num_in_int % (10 ** 6) != 0:
            temp = format(num_in_int / (10 ** 6), ".1f")
        else:
            temp = int(num_in_int / (10 ** 6))

        str_num = str(temp) + "M"

    # print(str_num)

    return str_num


def search(request):
    # order_by will give us an object(key:value) pair
    search_tubers = Influencer.objects.order_by("-created_date")

    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            search_tubers = search_tubers.filter(name__icontains=keyword)

    data = {
        "search_tubers": search_tubers,
    }
    return render(request, "influencers/search.html", data)

    # function to dump the data into json file with channel name as filename
    def dump(self):
        if self.channel_statistics is None or self.video_data is None:
            print("DATA is NONE")
            return

        fused_data = {
            self.channel_id: {
                "channel_statistics": self.channel_statistics,
                "video_data": self.video_data,
            }
        }

        channel_title = self.video_data.popitem()[1].get(
            "channelTitle", self.channel_id
        )  # get channel name from data
        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + ".json"
        with open(file_name, "w") as f:
            json.dump(fused_data, f, indent=4)

        print("File Dumped")


# def Brands(request):
#     return render(request, "accounts/brands/brands.html")
