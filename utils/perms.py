def is_mod_or_admin(message):
    perms = message.author.server_permissions
    return perms.manage_roles or perms.administrator
