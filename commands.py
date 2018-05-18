import discord
from settings import ROLES, TITLES, MESSAGES
from discord.utils import get
from utils.utils import is_mod_or_admin


async def help_cmd(bot, message):
    help_embed = discord.Embed(title='Help', type='rich', description="Commands: help, init", color=0xffffff)
    await bot.send_message(message.channel, embed=help_embed)


async def init(bot, message):
    if not is_mod_or_admin(message):
        await bot.send_message(message.channel, "Must be mod or admin to initiate")
    else:
        await bot.send_message(message.channel, "Initiating...")

        i = 0
        for msg in MESSAGES:
            init_embed = discord.Embed(title=TITLES[i], type='rich', description=msg, color=0xffffff)
            init_message = await bot.send_message(message.channel, embed=init_embed)
            curr_roles = ROLES[i][1]
            for key, emoji in curr_roles.items():
                reaction = get(bot.get_all_emojis(), name=emoji)
                if reaction is None:
                    reaction = emoji
                await bot.add_reaction(init_message, reaction)
            i = i + 1
