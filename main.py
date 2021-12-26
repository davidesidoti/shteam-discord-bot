import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', help_command=None)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.change_presence(activity=discord.Game(name='Rewriting my code x_x || -help'))


@bot.command()
async def help(ctx, arg=None):
    if arg == None:
        await ctx.send('help completo')
    else:
        await ctx.send('help specifico')


bot.run('ODIyNTMzMDY0NTE2ODI5MjA0.YFTpnA.BE8U2Micx7hlT8U5AKfTaStNbzE')
