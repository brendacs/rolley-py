import discord
from utils.config import ROLES
from utils.embeds import get_embeds
from utils.perms import is_mod_or_admin


async def help_cmd(bot, message):
    """ Prints a help message in the channel """

    help_embed = discord.Embed(title='Help', type='rich', description="Commands: help, init", color=0xffffff)
    await bot.send_message(message.channel, embed=help_embed)


async def init(bot, message):
    if not is_mod_or_admin(message):
        await bot.send_message(message.channel, "Must be mod or admin to initiate")
    else:
        await bot.send_message(message.channel, "Initiating...")

        all_embeds = get_embeds()
        for emb in all_embeds:
            init_msg = await bot.send_message(message.channel, embed=emb)

            for group in ROLES.values():    # Retrives sub-dicts
                for emoji in group.keys():
                    reaction = discord.utils.get(bot.get_all_emojis(), name=emoji)

                    # if reaction is not a default Discord reaction
                    if reaction is None:
                        reaction = emoji
                    await bot.add_reaction(init_msg, reaction)
