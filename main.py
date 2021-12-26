import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', help_command=None)

helpCommands = {'helpUsage': '`-help [(opt) command]`',
                'helpInfo': 'Show this message if no arguments are given or help for a specific message.',
                'pingUsage': '`-ping`', 'pingInfo': 'Reply with the latency of the bot in milliseconds.'}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.change_presence(activity=discord.Game(name='Rewriting my code x_x || -help'))


# !
# TODO help command
# TODO info command
# !

# HELP COMMAND
@bot.command()
async def help(ctx, arg=None):
    if arg is None:
        _embed = discord.Embed(title='Help', description='Need help with the commands? Read this message.',
                               color=0x1f8b4c)
        _embed.add_field(name=helpCommands['helpUsage'], value=helpCommands['helpInfo'], inline=False)
        _embed.add_field(name=helpCommands['pingUsage'], value=helpCommands['pingInfo'], inline=False)
        await ctx.send(embed=_embed)
    else:
        if arg.lower() == 'ping':
            _embed = discord.Embed(title='`-ping` help', color=0x1f8b4c)
            _embed.add_field(name=helpCommands['pingUsage'], value=helpCommands['pingInfo'], inline=False)
            await ctx.send(embed=_embed)


# PING COMMAND
@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'`Pong! ({round(bot.latency * 1000)}ms)`')


# SERVER INFO COMMAND
@bot.command()
async def serverinfo(ctx):
    membersInfo = {'Total Users': ctx.guild.member_count, 'Online Users': sum(
        member.status == discord.Status.online and not member.bot for member in ctx.guild.members),
                   'Offline Users': sum(
                       member.status == discord.Status.offline and not member.bot for member in ctx.guild.members),
                   'Human Members': sum(not member.bot for member in ctx.guild.members),
                   'Bot Members': sum(member.bot for member in ctx.guild.members)}
    channelsInfo = {"Total Categories": len(ctx.guild.categories), "Total Channels": len(ctx.guild.channels),
                    "Total Text Channels": len(ctx.guild.text_channels),
                    "Total Voice Channels": len(ctx.guild.voice_channels)}
    rolesInfo = {"Total Roles": len(ctx.guild.roles)}
    boostsInfo = {"Boost Level": ctx.guild.premium_tier, "Total Boosts": ctx.guild.premium_subscription_count}

    _embed = discord.Embed(title='Server Info', color=0x1f8b4c)
    _embed.add_field(name='Members Info',
                     value=f"Total Users: `{membersInfo['Total Users']}`\nOnline Users: `{membersInfo['Online Users']}`")
    await ctx.send(embed=_embed)


bot.run('ODIyNTMzMDY0NTE2ODI5MjA0.YFTpnA.BE8U2Micx7hlT8U5AKfTaStNbzE')
