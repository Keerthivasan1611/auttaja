import asyncio
import discord
import string

def on_message(cmd, args, message, app):
    app.reply(message.channel, "Command from {}\n cmd: `{}`\n args: `{}`".format(message.author.name, cmd, args))

def setup(bot, dclient, logger):
    logger.info("Setting up test command plugin")
    bot.register_command("testcmd", on_message)
