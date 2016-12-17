# Auttaja
Auttaja (finnish for helper) is a modular Python 3.5 Discord bot. Auttaja is just the core framework for creating an awesome bot. Modules can be enabled and disable on demand, and it comes with a full permissions system.

Please note, this is still very much a work in progress

[Add Auttaja to Your Server](https://discordapp.com/api/oauth2/authorize?client_id=242730576195354624&scope=bot&permissions=0)

## Quickstart
The best way to start is to take a look at some of the example plugins.  We will go over a few of the ideas behind the API here.  The API was designed to give you a full access to the Discord.py API while abstracting a few things away, such as commands and permissions.

### Event plugin
A basic plugin, which prints each message the bot sees to a log file, looks like this:

```python
def on_message(message, app):
    app.logger.info(message.content)

def setup(bot, dclient, logger):
    logger.info("Setting up message printing plugin")
    bot.register_callback("on_message", on_message)
```

Every plugin must have a setup function.  This is how you register callbacks for both discord events, and commands.  For the callback itself we chose to use the name "on\_message", because it was analagous to the discord.py name, but you can choose anything you want, since you register it.  The string that you register with, however, does need to match the discord.py event name.  Every event callback will take the same arguments as the discord.py event, with the addition of the "app" argument.  This exposes parts of the underlying bot so you can access discord.py directly, access logging, and use some helper functions that we provide.

### Command plugin
For command plugins, we see something very similar to the above, with a few changes to help extrapolate the parsing of commands away from the plugin developers, yay!

```python
def on_message(cmd, args, message, app):
    app.reply(message.channel, "Command from {}\n cmd: `{}`\n args: `{}`".format(message.author.name, cmd, args))

def setup(bot, dclient, logger):
    logger.info("Setting up test command plugin")
    bot.register_command("testcmd", on_message)
```

The only real differences here are the arguments to the callback, and the function you use to register.  You pass in the command you want to register, along with the callback you want to get called.  The base bot parses out the command prefix, so you don't need to worry about that.  You are given the command, the arguments, the discord.py message object, and the underlying bot app class to give you full access to the discord.py client, `app.dclient`, and all of our helper functions.
Thats about all there is to it!  You can import any Python libraries you want and use them to your hearts content!!
