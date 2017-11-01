# Tyrone in Python
# Created By Aj

import discord
import logging
import Interface
import asyncio

tyrone = discord.Client()
@tyrone.event
async def on_ready():
    print('Connected')
    print('##########################')

@tyrone.event
async def on_message(message):
    if message.content.startswith('!test'):
       tyrone.send_message(message.channel, 'Hello! %s' % message.author)

Window = Interface.GUI()
tyrone.run("auth_token")

