# Rolley
A role-by-reacts role management bot for Discord.

## Set up

* Clone the repository and install dependencies using `pip install -r requirements.txt`. This bot requires Python 3.4.2+ to run smoothly.
* All configurations are set in `utils/config.py`.
* Create a channel for roles and configure the `HOST_CHANNEL` in your `config.py` to match the name of the channel created.
* Set `INACCESSIBLE_ROLES` to roles you do not want the users of the bot tampering with. Users will be unable to add and remove these roles from themselves.
* Set `ROLES` based on your server roles. Each role group will be assigned to a separate message. The role groups will stay in order only if they are alphabetically ordered (an inconvenience that will be fixed at a later time). `key: value` pairs should be in the format of `role: emoji`. If a custom emoji is being used, the `value` should be the exact name given to that emoji in the server.
* Set `EMBEDS` based on what you want you Discord embed messages to say. This is in the format of an array of tuples, `[(title, message), (title, message), ...]`. These should be done in order. Each one will be paired with your dictionary of roles and emojis in order as well.

## Usage

* Run `python3 main.py` to start the bot.
* The default prefix is `>`, but can be set in the `config.py` by changing the `PREFIX` string. This should only be one letter, number, or character. 
* Use the `help` command to list all commands.
* Use the `init` command to send the initial embed messages with attached reacts. Users can use the reacts to add and remove roles from themselves.
* All commands can only be used in the `HOST_CHANNEL` that should have been set earlier.
* The `init` command can only be used by mods (those with manage roles permissions) or admins (those with administrator permissions). This can be changed in `utils/perms.py`.
* Emojis outside of the ones set in your `config.py` cannot be added to an initial message's emoji list.
