import discord
from utils.config import ROLES, INACCESSIBLE_ROLES
from discord.utils import get


def reaction_to_role(reaction):
    emoji = reaction.emoji
    if reaction.custom_emoji:
        emoji = reaction.emoji.name

    for subgroup in ROLES.values():
        for r, e in subgroup.items():
            if e == emoji:
                return r
    return None


def user_has_role(user, role):
    for r in user.roles:
        if r.name == role or r == role:
            return True
    return False


# check if user already has role in category where they can only have one e.g., seniority
def user_has_single_use_category(user, *categories):
    for category in categories:
        for role_name in category:
            if user_has_role(user, role_name):
                return True
        return False


# check that role is not none and is a server role
def is_valid_role(user, role):
    for r in user.server.roles:
        if r.name == role:
            return True
    return False


# check if role is accessible
def is_accessible_role(role):
    if role in INACCESSIBLE_ROLES:
        return False
    return True


# adds a role to user
async def add_role(bot, user, role):
    seniority_roles = list(ROLES["seniorities"].keys())
    if not is_valid_role(user, role) or user_has_role(user, role) \
            or (user_has_single_use_category(user, seniority_roles)
                and role in seniority_roles):
        return

    try:
        role_to_add = get(user.server.roles, name=role)
        await bot.add_roles(user, role_to_add)
    except discord.Forbidden:
        await bot.send_message(user, "Please give bot Manage Role permissions or notify an admin")
        return


# removes a role from user
async def remove_role(bot, user, role):
    if not is_valid_role(user, role) or not user_has_role(user, role):
        return

    all_user_roles = user.roles
    for r in all_user_roles:
        if r.name == role:
            try:
                await bot.remove_roles(user, r)
            except discord.Forbidden:
                await bot.send_message(user, "Please give bot Manage Role permissions or notify an admin")
                return


# removes all roles from user
async def remove_all_roles(bot, user):
    all_user_roles = user.roles
    roles_to_remove = []
    for r in all_user_roles:
        if is_accessible_role(r.name):
            roles_to_remove.append(r)
    await bot.remove_roles(user, *roles_to_remove)
