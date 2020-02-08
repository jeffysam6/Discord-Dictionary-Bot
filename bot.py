
import os

import discord

import random

from discord.ext import commands

import json

import http.client

import random



token = "NjM2NjM1MDY1NDUwNzU4MTc0.XbH_fw.Apj2cCzGIR1Yu4tfcgS_WX2aPzg"

my_guild = "My Dome"




bot = commands.Bot(command_prefix="!")



@bot.command(name="roll_dice",help="Simulates rolling dice")
async def nine_nine(ctx,number_of_dice:int,number_of_sides:int):
    dice = [
            str(random.choice(range(1,number_of_sides + 1)))
            for _ in range(number_of_dice)
            ]

    await ctx.send(', '.join(dice))


@bot.command(name="search",help="Finds meaning from urban book dictionary")
async def dictionary(ctx,term):

    conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")
    headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "da4a52f89fmshc2b5e9799146441p100937jsn02c9fc45bc4d"
    }
    conn.request("GET", f"/define?term={term}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    d = json.loads(data.decode('utf-8'))
    defin = []
    for i in d['list']:
        defin.append(i["definition"])
    await ctx.send(random.choice(defin))



@bot.command(name="create-channel")
@commands.has_role("admin")
async def create_channel(ctx,channel_name="python"):

    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels,name=channel_name)

    if not existing_channel:
        print(f"Creating a new channel: {channel_name}")
        await guild.create_text_channel(channel_name)



@bot.event
async def on_command_error(ctx,error):

    if isinstance(error,commands.error.CheckFailure):
        await ctx.send('You do noot have the correct role for this command')

bot.run(token)




# client = discord.Client()


# @client.event
# async def on_ready():

#     guild = discord.utils.get(client.guilds,name=my_guild)

#     print(
#         f"{client.user} is connected to the following guild:\n"
#         f"{guild.name}(id:{guild.id})"
#         )


# @client.event
# async def on_member_join(member):

#     await member.create_dm()
#     await member.dm_channel.send(
#         f"Hi {member.name},Welcome to my server!")



# @client.event
# async def on_message(message):
#     if(message.author == client.user):
#         return


#     stoic_quote = [
#     'I \'m the lord your god blow up.',
#     'Everything is so sad',
#     'okay my bad']


#     if(message.content == "stoic"):
#         response = random.choice(stoic_quote)

#         await message.channel.send(response)


#     elif message.content == 'raise-exception':
#         raise discord.DiscordException



# client.run(token)