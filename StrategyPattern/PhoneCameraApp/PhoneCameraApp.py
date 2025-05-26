import abc
from StrategyPattern.PhoneCameraApp.SharePic import ShareText, ShareEmail, ShareSocialMedia


class PhoneCameraApp:
    def __init__(self, name):
        self.pic_name = None
        self.name = name

    def take(self):
        print(f"{self.name} took a picture!")

    @abc.abstractmethod
    def edit(self):
        pass

    def save(self, pic_name):
        self.pic_name = pic_name
        print(f"{self.name} saved picture '{self.pic_name}'!")

    def share_text(self):
        ShareText.share(self)

    def share_email(self):
        ShareEmail.share(self)

    def share_social_media(self):
        ShareSocialMedia.share(self)
