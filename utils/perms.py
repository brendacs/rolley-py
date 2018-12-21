def is_mod_or_admin(author):
    perms = author.server_permissions
    return perms.manage_roles or perms.administrator
