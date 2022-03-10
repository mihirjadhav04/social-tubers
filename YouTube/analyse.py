import json
import pandas as pd

file = "mihir_jadhav.json"
data = None

with open(file, "r") as f:
    data = json.load(f)

channel_id, stats = data.popitem()
print(channel_id)

channel_stats = stats["channel_statistics"]
video_stats = stats["video_data"]


# Channel Statistics
print("views :", channel_stats["viewCount"])
print("subscriber :", channel_stats["subscriberCount"])
print("videos :", channel_stats["videoCount"])


# Video Statistics
# Sort video data according to the view count
sorted_videos = sorted(
    video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True
)
stats = []
for vid in sorted_videos:
    video_id = vid[0]
    title = vid[1]["title"]
    views = vid[1]["viewCount"]
    likes = vid[1]["likeCount"]
    comments = vid[1]["commentCount"]
    stats.append(
        [
            title,
            views,
            likes,
            comments,
        ]
    )
df = pd.DataFrame(
    stats,
    columns=[
        "title",
        "views",
        "likes",
        "comments",
    ],
)
print(df.head(10))
