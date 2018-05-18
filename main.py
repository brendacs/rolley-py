import discord
from settings import TOKEN, PREFIX
import commands
from utils.utils import add_role, reaction_to_role

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

    if message.content.startswith(PREFIX):
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

    # TODO: check which channel this is being done in
    # TODO: check if one of the clearing emojis were clicked -> remove_all_roles
    role = reaction_to_role(reaction)
    await add_role(bot, user, role)


# TODO: on_reaction_remove

bot.run(TOKEN)
