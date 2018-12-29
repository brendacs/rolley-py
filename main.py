import os
from os.path import join, dirname
from dotenv import load_dotenv

from discord import Game
from discord.utils import get
from discord.ext.commands import Bot

from utils.config import PREFIX, HOST_CHANNEL, ROLES
from utils.utils import should_ignore
from utils.roles import add_role, get_role_from_reaction, remove_role, remove_all_roles
from utils.emojis import get_emoji_from_reaction, is_clearing_emoji, is_listed_emoji
import commands

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')

bot = Bot(command_prefix=PREFIX)
bot.remove_command('help')


async def run_cleanup():
    """ Removes all bot messages from HOST_CHANNEL and re-initiates """

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
    """ When reaction is added, dispatch correct action """

    if not should_ignore(bot, reaction.message.channel, user):
        emoji = get_emoji_from_reaction(reaction)

        # if a clearing emoji was clicked, remove all roles
        if is_clearing_emoji(emoji):
            await remove_all_roles(bot, user)

        # if emoji was not already listed, remove
        elif not is_listed_emoji(emoji):
            await bot.remove_reaction(reaction.message, reaction.emoji, user)

        else:
            role = get_role_from_reaction(reaction)
            await add_role(bot, user, role)


@bot.event
async def on_reaction_remove(reaction, user):
    """ When user removes reaction, remove role from user """

    if not should_ignore(bot, reaction.message.channel, user):
        role = get_role_from_reaction(reaction)
        await remove_role(bot, user, role)


@bot.command(name='help', description='returns info on all commands', brief='returns all usable commands',
             pass_context=True)
async def help(ctx, *args):
    if not should_ignore(bot, ctx.message.channel, ctx.message.author):
        if len(args) == 0:
            await commands.help_cmd(bot, ctx)
        else:
            await commands.help_cmd(bot, ctx, args)


@bot.command(name='initialize', description='initializes bot in channel', aliases=['init'],
             brief='bot start-up process', pass_context=True)
async def init(ctx):
    if not should_ignore(bot, ctx.message.channel, ctx.message.author):
        await commands.init(bot, ctx.message.channel, ctx.message.author)


bot.run(TOKEN)
