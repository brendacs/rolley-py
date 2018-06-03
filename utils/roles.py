import discord
from settings import ROLES
from discord.utils import get


def reaction_to_role(reaction):
    emoji = reaction.emoji
    if reaction.custom_emoji:
        emoji = reaction.emoji.name

    role = None
    for i in range(len(ROLES)):
        curr_roles = ROLES[i][1]
        for r, e in curr_roles.items():
            if e == emoji:
                role = r
    return role


def user_has_role(user, role):
    user_roles = []
    for r in user.roles:
        user_roles.append(r.name)
    return role in user_roles


# TODO: check if user already has role in category where they can only have one e.g., seniority


async def add_role(bot, user, role):
    if user_has_role(user, role):
        return

    serv_roles = []
    for r in user.server.roles:
        serv_roles.append(r.name)

    if role is None or role not in serv_roles:
        return

    try:
        role_to_add = get(user.server.roles, name=role)
        await bot.add_roles(user, role_to_add)
    except discord.Forbidden:
        # TODO: bot should DM user to add permissions for bots
        return

# TODO: remove_role


# TODO: remove_all_roles


# TODO: helper to check if any roles user has are not self-assignable -> do not remove these in remove_all_roles
