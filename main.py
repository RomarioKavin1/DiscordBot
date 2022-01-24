import discord

client=discord.Client()

@client.event
async def on_ready():
  print("we hav e logged in as {0.user}".format(client))


@client.evemt
async def say_hello(message):
  if message.author==client.user:
    return
  
  if 