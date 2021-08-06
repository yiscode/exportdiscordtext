from keepwake import keep_alive
import discord
import os
from fetchannel import fetchannel
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
    
    
    await message.channel.send(file=discord.File('file.txt'))
    os.remove('file.txt')
  
keep_alive()
client.run(os.getenv('TOKEN'))