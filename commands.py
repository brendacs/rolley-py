import discord
from utils.config import ROLES, EMBEDS
from discord.utils import get
from discord.ext.commands import HelpFormatter
from utils.perms import is_mod_or_admin


async def help_cmd(bot, ctx, *args):
    formatter = HelpFormatter()

    if len(args) == 0:
        pages = bot.formatter.format_help_for(ctx, bot)
    else:
        cmd_str = args[0][0]
        command = bot.commands.get(cmd_str)

        if command is None:
            emb = discord.Embed(title='Command: {}'.format(cmd_str), type='rich',
                                description='Invalid command entered', color=0xff0000)
            await bot.send_message(ctx.message.channel, embed=emb)
            return
        else:
            pages = bot.formatter.format_help_for(ctx, command)
    for page in pages:
        await bot.send_message(ctx.message.channel, page)


async def init(bot, channel, user):
    if not is_mod_or_admin(user):
        await bot.send_message(channel, "Must be mod or admin to initiate")
    else:
        await bot.send_message(channel, "Initiating...")

        for i in range(len(EMBEDS)):
            title, message = 0, 1
            init_embed = discord.Embed(title=EMBEDS[i][title], type='rich',
                                       description=EMBEDS[i][message], color=0xffffff)
            init_message = await bot.send_message(channel, embed=init_embed)

            role_group = sorted(ROLES.keys())[i]
            curr_roles = ROLES[role_group]
            for r, emoji in curr_roles.items():
                reaction = get(bot.get_all_emojis(), name=emoji)
                # if reaction is not a default Discord reaction
                if reaction is None:
                    reaction = emoji
                await bot.add_reaction(init_message, reaction)
