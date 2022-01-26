import discord
import os
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import discord.ext.commands as commands
client = discord.Client()
DiscordComponents(client)
@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod_mail")
    
    if message.author == client.user:
        return
    if str(message.channel.type) == "private" or (str(message.channel) == "help_channel"and message.content.startswith("h:")):
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        elif (str(message.channel) == "help_channel"and message.content.startswith("h:")):
            index = message.content.index(":")+1
            string = message.content
            help_message = string[index:]
            await modmail_channel.send("[" + message.author.display_name + "] " + help_message)
        else:
           await ctx.send("hello", components = [
        [Button(label="Hi", style="3", emoji = "🥴", custom_id="button1"), Button(label="Bye", style="4", emoji = "😔", custom_id="button2")]
        ])
           await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "mod_mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)
client.run(os.environ['Token'])