from django.shortcuts import render
from accounts.models import Influencer, User
import pickle
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
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
    if request.method == "POST":
        model = pickle.load(
            open(staticfiles_storage.path('model/knn_model.pkl'), 'rb'))
        df = pd.read_csv(staticfiles_storage.path('model/data.csv'))
        query = request.POST['influencer']
        distances, indices = model.kneighbors(
            df.loc[(df['channel_title'] == query)].values[0][1:].reshape(1, -1), n_neighbors=6)
        for i in indices.flatten():
            print(i, df.iloc[i, 0])
        recommended_influencers = []
        user = User.objects.get(name=query)
        recommended_influencers.append(user.influencer)
        for i in indices.flatten():
            if len(recommended_influencers) == 6:
                break
            u = User.objects.get(name=df.iloc[i,0])
            if u.influencer not in recommended_influencers:
                recommended_influencers.append(u.influencer)
        print(recommended_influencers)
        data = {
            "all_tubers": recommended_influencers,
        }
        return render(request, "webpages/search.html", data)

    return render(request, "webpages/search.html")
