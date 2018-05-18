from settings import ROLES


def is_mod_or_admin(message):
    perms = message.author.server_permissions
    return perms.manage_roles or perms.administrator


# TODO: move the below to a separate role handler


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


def add_role(bot, user, role):
    if user_has_role(user, role):
        return

    role_to_add = None
    for r in user.server.roles:
        if r.name == role:
            role_to_add = r
            break
    bot.add_roles(user, role_to_add)


# TODO: remove_role

# TODO: remove_all_roles

# TODO: helper to check if any roles user has are not self-assignable -> do not remove these in remove_all_roles
