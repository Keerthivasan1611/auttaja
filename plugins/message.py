import asyncio
import discord
import string

def on_message(message, app):
    app.logger.info(message.content)

def setup(bot, dclient, logger):
    logger.info("Setting up message printing plugin")
    bot.register_callback("on_message", on_message)
