import discord 
from discord.ext import commands
import os

PREFIX = '.'

client = commands.Bot(command_prefix = PREFIX )

#words
bad_words = ['suchka','blyat','blya','suka','pizdec','blat','emae','idi naxuy','nax','pidaras','ebal', 'eblan','ebanutiy','fuck','fuck off','shit','ueban','shut up','ass','pussy','hole','gandon','zaebis','zaebal','asshole']

@client.event 

async def on_ready():
    print('[~]Bot By Trippingcarpet[~]')
    print('Version: 1.0.0')

@client.event

async def on_message(message):
    msg = message.content.lower().split()

    try:

        for n in msg:
            if n in bad_words:        
                await message.delete()
                await message.channel.send('BAD WORD DETECTED {0.author.mention}'.format(message))

    except:
        pass


client.run(os.environ['token'])
