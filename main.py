import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Można banować')

@client.command(pass_ctx=True)
@commands.has_permissions(ban_members=True)
async def Voteban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'{member} ZBANOWANY XDDD!!!')

@client.command()
async def rajdówki(ctx):
  await ctx.send('Rajdówki nie driftują')

@client.command()
async def golf(ctx):
  await ctx.send('Ej chłopaki golfa kupiłem')

@client.command()
async def mokotów(ctx):
  await ctx.send('Ej chłopaki mokotów, mokotów mnie goni')

@client.command()
async def mute(ctx):
  await ctx.send('No odmutujcie mnie no')

@client.command()
async def Pomocy(ctx):
  await ctx.send('mute')
  await ctx.send('golf')
  await ctx.send('rajdówki')
  await ctx.send('Voteban')
  await ctx.send('mokotów')

keep_alive()
client.run(os.getenv('TOKEN'))