# Tyrone in Python
# Created By Antwaun Tune

import discord
import logging
import Interface
import asyncio

tyrone = discord.Client()
@tyrone.event
async def on_ready():
    print('Connected')
    print(tyrone.user.name)
    print(tyrone.user.id)
    print('##########################')

Window = Interface.GUI()
tyrone.run("MzAwODczNTk0OTYyMDUxMDcz.DNqaGQ.U7Ygf7JhEhTaVKDOR1Cab5OMZ-k")
