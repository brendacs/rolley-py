from settings import EMBEDS


class Embed(object):
    def __init__(self, title="", description=""):
        self.title = title
        self.message = description

    @staticmethod
    def create_embeds():
        all_paired_embeds = []
        for i in range(len(EMBEDS) - 1):
            all_paired_embeds.append(Embed(EMBEDS[i], EMBEDS[i + 1]))
        return all_paired_embeds
