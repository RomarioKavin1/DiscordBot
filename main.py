import discord
import os
client=discord.Client()

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #elif message.content.startswith("$hello"):
    #await message.channel.send("Hello!")
  if str(message.channel.type=="private"):
    modmail_channel=discord.utils.get(client.get_all_channels(),name="mod_mail")
    await modmail_channel.send("["+message.author.display_name+"]"+message.content)
  elif str(message.channel)== "mod_mail" and message.content.startswith("<"):
    member_object=message.mentions[0]

    index= message.content.index(" ")
    string= message.content
    mod_message=string[index:]

    await member_object.send(("["+message.author.display_name+"]"+mod_message))
client.run(os.environ['Token'])
