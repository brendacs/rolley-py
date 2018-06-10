import discord
from config import ROLES, INACCESSIBLE_ROLES
from emojis import get_emoji_from_reaction

PERM_ERR_MSG = "Please give bot Manage Role permissions or notify an admin"

def get_role_from_reaction(reaction):
    """ previously named: reaction_to_role """

    emoji = get_emoji_from_reaction(reaction)

    for group in ROLES.values():
        if emoji in group:
            return group[emoji]     # role label
    return None

def user_has_role(user, role):
    for r in user.roles:
        if r.name == role or r == role:
            return True
    return False


# check that role is a valid server role
def is_valid_role(user, role):
    for r in user.server.roles:
        if r.name == role:
            return True
    return False


# check if user already has role in category where they can only have one e.g., seniority
def user_has_single_use_category(user, category):
    for role in category:
        if user_has_role(user, role):
            return True
    return False


# check if role is accessible
def is_accessible_role(role):
    return role not in INACCESSIBLE_ROLES

# adds a role to user
async def add_role(bot, user, role):
    seniority_roles = ROLES["seniorities"].values()
    if is_valid_role(user, role) \
       and not user_has_role(user, role) \
       and not user_has_single_use_category(user, seniority_roles):

        try:
            role_to_add = discord.utils.get(user.server.roles, name=role)
            await bot.add_roles(user, role_to_add)
        except discord.Forbidden:
            await bot.send_message(user, PERM_ERR_MSG)
            return


# removes a role from user
async def remove_role(bot, user, role):
    if user_has_role(user, role):
        for r in user.roles:
            if r.name == role:
                try:
                    await bot.remove_roles(user, r)
                except discord.Forbidden:
                    await bot.send_message(user, PERM_ERR_MSG)
                    return


# removes all roles from user
async def remove_all_roles(bot, user):
    all_user_roles = user.roles
    roles_to_remove = []
    for r in all_user_roles:
        if is_accessible_role(r.name):
           roles_to_remove.append(r)
    await bot.remove_roles(user, *roles_to_remove)
