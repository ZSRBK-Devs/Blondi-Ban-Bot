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
    await ctx.send('Blondi Zbanowany XDDD!!')

@client.command()
async def rajdówki(ctx):
  await ctx.send('Rajdówki nie driftują')

@client.command()
async def golf(ctx):
  await ctx.send('Ej chłopaki golfa kupiłem')

keep_alive()
client.run(os.getenv('TOKEN'))