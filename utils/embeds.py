import discord
from config import EMBEDS

def _generate_embeds(data):
    """ Returns a list of discord.Embed objects generated from the input data """

    return [discord.Embed(title=t, description=d, type='rich', color=0xffffff) for t,d in data]

def get_embeds():
    """ Directly returns the list of Embed objects """
    
    return _generate_embeds(EMBEDS)

