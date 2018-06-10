from config import ROLES

def get_emoji_from_reaction(reaction):

    emoji = reaction.emoji
    if reaction.custom_emoji:
        emoji = reaction.emoji.name
    return emoji

def is_clearing_emoji(emoji):
    return emoji in ROLES['clears']

def get_all_listed_emojis():
    """ Returns all emojis (i.e.: the keys in each sub-dict of ROLES)

        This function no longer has a reason to exist since is_listed_emoji()
        has been re-written
    """

    all_emojis = []
    for group in ROLES.values():    # Retrieves sub-dicts
        group_keys = group.keys()
        all_emojis += group_keys

    return all_emojis

def is_listed_emoji(emoji):
    """ Checks if emoji exists in ROLES

        No dependence on get_all_listed_emojis()
    """

    for group in ROLES.values():    # Retrieves sub-dicts
        if emoji in group:
            return True

    return False    # emoji was not found as a key in any sub-dict

