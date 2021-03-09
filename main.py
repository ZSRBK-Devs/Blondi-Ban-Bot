import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Można banować')

@client.command()
async def Voteban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('Blondi Zbanowany XDDD!!')

keep_alive()
client.run(os.getenv('TOKEN'))