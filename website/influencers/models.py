from django.db import models
from datetime import datetime

# Create your models here.
# from ckeditor.fields import RichTextField


class Youtuber(models.Model):
    influencer_name = models.CharField(max_length=255)
    influencer_email = models.EmailField(default="example@gmail.com")
    youtube_channel_id = models.CharField(
        max_length=255, default="Add You Channel Id here"
    )
    influencer_short_description = models.TextField()
    profile_photo = models.ImageField(upload_to="media/ytubers/%Y/%m/")
    # short_intro = RichTextField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)


#  influencer_name = request.POST.get("influencer_name")
#         to_email = request.POST.get("influencer_email")
#         from_email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
class ContactInfluencer(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    influencer_name = models.CharField(max_length=255)
    influencer_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
