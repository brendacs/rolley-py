from utils.config import EMBEDS


class Embed(object):
    def __init__(self, title="", description=""):
        self.title = title
        self.message = description

    @staticmethod
    def create_embeds():
        title, message = 0, 1
        all_paired_embeds = []
        for i in range(len(EMBEDS)):
            all_paired_embeds.append(Embed(EMBEDS[i][title], EMBEDS[i][message]))
        return all_paired_embeds
