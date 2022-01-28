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
    mod = discord.utils.get(client.get_all_channels(), name="Mod Bot")
  
    if message.author == client.user:
        return
    if str(message.channel.type) == "private" or (str(message.channel) == "help_channel"and message.content.startswith("h:")):
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")
            await message.channel.send("HI "+message.author.display_name+"Your help request has been sent to the moderators,kindly wait for the reply which will be sent to your DM within 48 hrs :)")

            for file in files:
                await modmail_channel.send(file.url)
        elif (str(message.channel) == "help_channel"and message.content.startswith("h:")):
            index = message.content.index(":")+1
            string = message.content
            help_message = string[index:]
            await modmail_channel.send("[" + message.author.display_name + "] " + help_message)
            await message.channel.send("HI "+message.author.display_name+"Your help request has been sent to the moderators,kindly wait for the reply which will be sent to your DM within 48 hrs :)")
        else:
          b=await message.channel.send("Click the button below to send this message to the moderators,To cancel delete this message", components = [
        Button(label="Send", style="3", emoji = "✔", custom_id="button1")
        ])          
          interaction = await client.wait_for("button_click", check = lambda i: i.custom_id == "button1")
          await interaction.send(content = "Message sent to moderator", ephemeral=True)
          await modmail_channel.send("[" + message.author.display_name + "] " + message.content)
          await message.channel.send("HI "+message.author.display_name+" Your help request has been sent to the moderators,kindly wait for the reply which will be sent to your DM within 48 hrs :)")
          await b.edit(components = [])
          
                      
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