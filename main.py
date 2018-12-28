import os
from os.path import join, dirname
from dotenv import load_dotenv

from discord import Game
from discord.utils import get
from discord.ext.commands import Bot

from utils.config import PREFIX, HOST_CHANNEL, ROLES
from utils.roles import add_role, reaction_to_role, remove_role, remove_all_roles
from utils.emojis import get_emoji_from_reaction, is_clearing_emoji, is_listed_emoji
import commands

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')

bot = Bot(command_prefix=PREFIX)
bot.remove_command('help')


async def run_cleanup():
    print("Started cleanup")
    channel = get(bot.get_all_channels(), name=HOST_CHANNEL)
    if channel is None:
        print("Could not locate channel: {}".format(HOST_CHANNEL))
        return
    else:
        author = None
        async for message in bot.logs_from(channel):
            if message.author.id == bot.user.id:
                author = message.author
                await bot.delete_message(message)

        if author is None:
            print("Could not re-add reaction messages. Admin must manually run >init")
        else:
            await commands.init(bot, channel, author)
    print("Finished cleaning up {} channel".format(HOST_CHANNEL))


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="Leetcode"))
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    await run_cleanup()


@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    channel_reacted_in = reaction.message.channel.name
    if channel_reacted_in != HOST_CHANNEL:
        return

    emoji = get_emoji_from_reaction(reaction)

    # if a clearing emoji was clicked, remove all roles
    if is_clearing_emoji(emoji):
        await remove_all_roles(bot, user)

    # if emoji was not already listed, remove
    elif not is_listed_emoji(emoji) and channel_reacted_in == HOST_CHANNEL:
        await bot.remove_reaction(reaction.message, reaction.emoji, user)

    else:
        role = reaction_to_role(reaction)
        await add_role(bot, user, role)


@bot.event
async def on_reaction_remove(reaction, user):
    if user == bot.user:
        return
    role = reaction_to_role(reaction)
    await remove_role(bot, user, role)


@bot.command(name='help', description='returns info on all commands', brief='returns all usable commands',
             pass_context=True)
async def help(ctx, *args):
    if ctx.message.channel.name == HOST_CHANNEL:
        if len(args) == 0:
            await commands.help_cmd(bot, ctx)
        else:
            await commands.help_cmd(bot, ctx, args)


@bot.command(name='initialize', description='initializes bot in channel', aliases=['init'],
             brief='bot start-up process', pass_context=True)
async def init(ctx):
    if ctx.message.channel.name == HOST_CHANNEL:
        await commands.init(bot, ctx.message.channel, ctx.message.author)


bot.run(TOKEN)
