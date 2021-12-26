import discord
from discord.ext import commands

intents = discord.Intents()
intents.all()
bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)

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
    # MEMBERS COUNT
    _onlineMembers = 0
    _offlineMembers = 0
    _humanMembers = 0
    _botMembers = 0
    for member in ctx.guild.members:
        if member.bot:
            _botMembers += 1
            print(f'{member.name} bot')
            continue
        else:
            _humanMembers += 1
            if member.status == discord.Status.online:
                print("online")
                _onlineMembers += 1
                continue
            elif member.status == discord.Status.offline:
                _offlineMembers += 1
                continue

    channelsInfo = {"Total Categories": len(ctx.guild.categories), "Total Channels": len(ctx.guild.channels),
                    "Total Text Channels": len(ctx.guild.text_channels),
                    "Total Voice Channels": len(ctx.guild.voice_channels)}
    rolesInfo = {"Total Roles": len(ctx.guild.roles)}
    boostsInfo = {"Boost Level": ctx.guild.premium_tier, "Total Boosts": ctx.guild.premium_subscription_count}

    _embed = discord.Embed(title='Server Info', color=0x1f8b4c)
    _embed.add_field(name='Members Info',
                     value=f"Total Users: `{ctx.guild.member_count}`\nOnline Users: `{_onlineMembers}`\nOffline Users: `{_offlineMembers}`\nHuman Users: `{_humanMembers}`\nBot Users: `{_botMembers}`")
    await ctx.send(embed=_embed)


bot.run('ODIyNTMzMDY0NTE2ODI5MjA0.YFTpnA.BE8U2Micx7hlT8U5AKfTaStNbzE')
