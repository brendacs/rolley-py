import discord
from utils.config import ROLES
from utils.embeds import Embed
from discord.utils import get
from discord.ext.commands import HelpFormatter
from utils.perms import is_mod_or_admin


formatter = HelpFormatter()


async def help_cmd(bot, ctx):
    pages = bot.formatter.format_help_for(ctx, bot)
    for page in pages:
        await bot.send_message(ctx.message.channel, page)


async def init(bot, message):
    if not is_mod_or_admin(message):
        await bot.send_message(message.channel, "Must be mod or admin to initiate")
    else:
        await bot.send_message(message.channel, "Initiating...")

        all_paired_embeds = Embed.create_embeds()
        for i in range(0, len(all_paired_embeds)):
            init_embed = discord.Embed(title=all_paired_embeds[i].title, type='rich',
                                       description=all_paired_embeds[i].message, color=0xffffff)
            init_message = await bot.send_message(message.channel, embed=init_embed)

            role_group = list(sorted(ROLES.keys()))[i]
            curr_roles = ROLES[role_group]
            for r, emoji in curr_roles.items():
                reaction = get(bot.get_all_emojis(), name=emoji)
                # if reaction is not a default Discord reaction
                if reaction is None:
                    reaction = emoji
                await bot.add_reaction(init_message, reaction)
