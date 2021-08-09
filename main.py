from keepwake import keep_alive
import discord
import os
from fetchannel import fetchannel
from fetchannel import convertdocx as cod

client = discord.Client()
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if '!export' in message.content:
    
    await fetchannel(message)
    await cod(message)
    
    await message.channel.send(file=discord.File('file.txt'))
    await message.channel.send(file=discord.File('demo.docx'))
    os.remove('file.txt')
    os.remove('demo.docx')
  
keep_alive()
client.run(os.getenv('TOKEN'))