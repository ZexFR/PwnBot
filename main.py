import discord 
from discord.ext import commands
import requests
import asyncio
import time
import os

PwnBot = commands.Bot(command_prefix = ">")
PwnBot.remove_command('help')
intents = discord.Intents.default()
intents.members = True


@PwnBot.event
async def on_ready():   
    await PwnBot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over Sem Wrld"))
print("Logged in.")



@PwnBot.command()
async def webhost(ctx,word):
    list = []
    with open("webhost.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on 000webhost.com\n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")

@PwnBot.command()
async def fivepx(ctx,word):
    list = []
    with open("500px.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on 500px.com \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")

@PwnBot.command()
async def eighttracks(ctx,word):
    list = []
    with open("8track.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on 8Tracks.com \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")

@PwnBot.command()
async def abandonia(ctx,word):
    list = []
    with open("abandonia.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on Abandonia.com \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")

@PwnBot.command()
async def epicgames(ctx,word):
    list = []
    with open("epicgames.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on Epicgames.com \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")




@PwnBot.command()
async def imgur(ctx,word):
    list = []
    with open("imgur.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on Imgur.com \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")

@PwnBot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
         color = discord.Color.dark_blue()
    )
    
    embed.set_author(name="Help")
    embed.add_field(name=">search", value="Searches all the db's for the email you provide!", inline=False)
    embed.add_field(name=">eighttracks", value="Gives you the search of db for 8track.com", inline=False)
    embed.add_field(name=">webhost", value="Gives you the search of db for 000webhost.com", inline=False)
    embed.add_field(name=">fivepx", value="Gives you the search of db for 500px.com", inline=False)
    embed.add_field(name=">epicgames", value="Gives you the search of db for epicgames.com", inline=False)
    embed.add_field(name=">whitepages", value="Gives you the search of db for whitepages.com", inline=False)
    embed.add_field(name=">imgur", value="Gives you the search of db for imgur.com", inline=False)
    
    await ctx.channel.send(embed=embed)

@PwnBot.command()
async def whitepages(ctx,word):
    list = []
    with open("white.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on Whitepages.com \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")

@PwnBot.command()
async def search(ctx,word):
    list = []
    with open("all.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    list.append(part)

    o = open("result.txt", "w+")
    o.write(f"Results for {word} on all of the databases \n \n")
    o.write("\nl".join(list))
    o.close()
    await ctx.send(file=discord.File("result.txt"))
    os.remove("result.txt")



PwnBot.run("OTAyOTM4MDEzNzYyNDU3Njcx.YXlsjg.JhaSCD0SulemU_68Qbn3UCO9pC0")
