class SharePic:
    def share(self):
        pass


class ShareText(SharePic):
    def share(self):
        print(f"'{self.pic_name}' Shared via Text")


class ShareEmail(SharePic):
    def share(self):
        print(f"'{self.pic_name}' Shared via Email")


class ShareSocialMedia(SharePic):
    def share(self):
        print(f"'{self.pic_name}' Shared via Social Media")
