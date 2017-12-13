# Tyrone in Python
# Created By Aj

import discord
import logging
import asyncio

tyrone = discord.Client()

@tyrone.event
async def on_message(message):
    if message.author == tyrone.user:
        return

    if (message.content.lower().startswith('hello')) or (message.content.lower().startswith('hi')) or (message.content.lower().startswith('hey')):
        msg_txt = 'Hello {0.author.mention}'.format(message)
        await tyrone.send_message(message.channel, msg_txt)

@tyrone.event
async def on_ready():
    print('Connected')
    await tyrone.logout()
