import discord
from utils.config import PREFIX, HOST_CHANNEL, ROLES
import commands
from utils.roles import add_role, reaction_to_role, remove_role, remove_all_roles
from os.path import join, dirname
from dotenv import load_dotenv
import os

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

    # TODO: check if one of the clearing emojis were clicked -> remove_all_roles
    clearing_emojis = list(ROLES["clears"].values())
    if reaction.emoji in clearing_emojis or reaction.custom_emoji in clearing_emojis:
        await remove_all_roles(bot, user)

    # TODO: check if reaction is not already listed -> do not add or remove
    role = reaction_to_role(reaction)
    await add_role(bot, user, role)


@bot.event
async def on_reaction_remove(reaction, user):
    if user == bot.user:
        return
    role = reaction_to_role(reaction)
    await remove_role(bot, user, role)

bot.run(TOKEN)
