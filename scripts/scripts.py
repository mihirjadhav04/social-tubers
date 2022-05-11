import csv
from accounts.models import User, Influencer
from django.core.files import File

if __name__ == "__main__":
    print("here")

    def run():

        # Influencer.objects.all().delete()

        with open('./apnawala.csv', encoding='cp437') as file:
            reader = csv.reader(file)
            next(reader)  # Advance past the header
            for row in reader:
                user = User(name=row[0],email=row[7],is_influencer=True)
                user.save()
                influencer = Influencer(user=user,channel_name=row[6],youtube_id=row[10],category_type=row[8],short_description=row[9])
                influencer.profile_photo.save('temp.png', File(open('C:/Users/Lenovo/OneDrive/Desktop/Ronak/LYP-main2/website/influencers/download.png', 'rb')))
                influencer.save()

        print("done")

    run()
