from os.path import join, dirname
from dotenv import load_dotenv
import os
import discord
from utils.config import PREFIX, HOST_CHANNEL, ROLES
from utils.roles import add_role, reaction_to_role, remove_role, remove_all_roles
from utils.emojis import get_emoji_from_reaction, is_clearing_emoji, is_listed_emoji
import commands

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')

bot = discord.Client();


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(PREFIX) \
            and message.channel.name == HOST_CHANNEL:
        command = message.content[1:]
        if command == 'help':
            await commands.help_cmd(bot, message)
        elif command == 'init':
            await commands.init(bot, message)
    else:
        return


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
    elif not is_listed_emoji(emoji):
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

bot.run(TOKEN)
