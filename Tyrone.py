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

Window = Interface.GUI()
tyrone.run("auth_token")
