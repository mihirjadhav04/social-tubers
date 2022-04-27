from instabot import Bot
import os
import shutil


def clean_up(i):
    dir = "config"
    remove_me = "{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):
    bot = Bot()

    bot.login(username="socialtubersofficial", password="@vscode#143$")
    bot.upload_photo("{}".format(i), caption="Socialtubers is thrilled to announce @mihirjadhav04 onboard with our company. We extend you warmest welcome and good wishes from the entire family and look forward to have an exciting influential journey with you ahead.")


if __name__ == '__main__':
    # enter name of your image bellow
    image_name = "aman.jpg"
    clean_up(image_name)
    upload_post(image_name)