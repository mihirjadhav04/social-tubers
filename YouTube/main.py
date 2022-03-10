from youtube_stats import YTstats


API_KEY = "AIzaSyCGEy4EZ4XinMU1voULK5GmZ5DBDE2OVp0"
channel_id = "UCSegc_0vxRuyJDw_vKGVPmA"


# object of YTstats as yt
yt = YTstats(API_KEY, channel_id)
data = yt.get_channel_statistics()
print(data)

yt.get_channel_video_data()
# print(data)
yt.dump()
