import time

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import difflib

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='-', help_command=None)

helpCommands = {'helpUsage': '`-help [(opt) command]`',
                'helpInfo': 'Show this message if no arguments are given or help for a specific message.',
                'pingUsage': '`-ping`', 'pingInfo': 'Reply with the latency of the bot in milliseconds.',
                'serverinfoUsage': '`-serverinfo`',
                'serverinfoInfo': 'Show a list of some useful informations about the server.'}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.change_presence(activity=discord.Game(
        name='"Yesterday is history. Tomorrow is a mistery. But today is a gift. That\'s why it is called present" || -help'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        _embed = discord.Embed(title='Error: command not found.',
                               description='Sorry but I could not find that command. Type `-help` for a list of '
                                           'commands.',
                               color=0x2ecc71)
        await ctx.send(embed=_embed)
    raise error


# HELP COMMAND
@bot.command()
async def help(ctx, arg=None):
    if arg is None:
        _embed = discord.Embed(title='Help', description='Need help with the commands? Read this message.',
                               color=0x1abc9c)
        _embed.add_field(name=helpCommands['helpUsage'], value=helpCommands['helpInfo'], inline=False)
        _embed.add_field(name=helpCommands['pingUsage'], value=helpCommands['pingInfo'], inline=False)
        _embed.add_field(name=helpCommands['serverinfoUsage'], value=helpCommands['serverinfoInfo'], inline=False)
        await ctx.send(embed=_embed)
    else:
        if arg.lower() == 'ping':
            _embed = discord.Embed(title='`-ping` help', color=0x1abc9c)
            _embed.add_field(name=helpCommands['pingUsage'], value=helpCommands['pingInfo'], inline=False)
            await ctx.send(embed=_embed)
        elif arg.lower() == 'serverinfo':
            _embed = discord.Embed(title='`-serverinfo` help', color=0x1abc9c)
            _embed.add_field(name=helpCommands['serverinfoUsage'], value=helpCommands['serverinfoInfo'], inline=False)
            await ctx.send(embed=_embed)
        else:
            _embed = discord.Embed(title=f'Command not found!', color=0x1abc9c)
            _embed.add_field(name=f'Command `{arg.lower()}` not found!',
                             value=f'Sorry but I could not find the command `{arg.lower()}`.')
            await ctx.send(embed=_embed)


# PING COMMAND
@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'`Pong! ({round(bot.latency * 1000)}ms)`')


# SERVER INFO COMMAND
@bot.command()
async def serverinfo(ctx):
    membersInfo = {'Total Members': ctx.guild.member_count, 'Online Members': sum(
        member.status != discord.Status.offline and not member.bot for member in ctx.guild.members),
                   'Offline Members': sum(
                       member.status == discord.Status.offline and not member.bot for member in ctx.guild.members),
                   'Human Members': sum(not member.bot for member in ctx.guild.members),
                   'Bot Members': sum(member.bot for member in ctx.guild.members)}
    channelsInfo = {'Total Categories': len(ctx.guild.categories), 'Total Channels': len(ctx.guild.channels),
                    'Total Text Channels': len(ctx.guild.text_channels),
                    'Total Voice Channels': len(ctx.guild.voice_channels)}
    rolesInfo = {'Total Roles': len(ctx.guild.roles)}
    boostsInfo = {'Boost Level': ctx.guild.premium_tier, 'Total Boosts': ctx.guild.premium_subscription_count}

    _embed = discord.Embed(title='Server Info', color=0x11806a)
    _embed.add_field(name='-- Members Info --',
                     value=f"Total Users: `{membersInfo['Total Members']}`\nOnline Users: `{membersInfo['Online Members']}`\nOffline Users: `{membersInfo['Offline Members']}`\nHuman Users: `{membersInfo['Human Members']}`\nBot Users: `{membersInfo['Bot Members']}`",
                     inline=False)
    _embed.add_field(name='-- Channels Info --',
                     value=f"Total Channels: `{channelsInfo['Total Channels']}`\nTotal Categories: `{channelsInfo['Total Categories']}`\nTotal Text Channels: `{channelsInfo['Total Text Channels']}`\nTotal Voice Channels: `{channelsInfo['Total Voice Channels']}`",
                     inline=False)
    _embed.add_field(name='-- Roles Info --', value=f"Total Roles: `{rolesInfo['Total Roles']}`", inline=False)
    _embed.add_field(name='-- Boosts Info --',
                     value=f"Boost Level: `{boostsInfo['Boost Level']}`\nTotal Boosts: `{boostsInfo['Total Boosts']}`",
                     inline=False)
    await ctx.send(embed=_embed)


# WEB COMMAND
@bot.command()
async def tut(ctx, *, arg):
    # ! EMBED COLOR = 0x1f8b4c
    tutorials = ['list', 'center div', 'complete box shadow', 'mid box shadow']
    tutorial = difflib.get_close_matches(arg, tutorials)
    ###################################################################################################################
    if len(tutorial) == 0:
        _embed = discord.Embed(title=f'`{arg}` not found!',
                               description='Sorry but I could not find the tutorial you are looking for.',
                               color=0x1f8b4c)
        await ctx.send(embed=_embed)
    ###################################################################################################################
    elif len(tutorial) == 1:
        # ! PRINT LIST
        if tutorial[0] == 'list':
            _embed = discord.Embed(title='Tutorials list', color=0x1f8b4c)
            i = 0
            for tutor in tutorials:
                if tutorials.index(tutor) == 0:
                    continue
                i += 1
                embedText = f'{i} - `{tutor}`'
                _embed.add_field(name=embedText, value=f'Type `-tut {tutor}` to show this tutorial.', inline=False)
            await ctx.send(embed=_embed)
        # ! PRINT LIST

        # ! PRINT CENTER DIV TUTORIAL
        if tutorial[0] == 'center div':
            _embed = discord.Embed(title=f'How to: `{tutorial[0]}`',
                                   description='Type `-tut` followed by a tutorial you want to see to display it!',
                                   color=0x1f8b4c)
            _embed.add_field(name='HTML', value='''
```html
<div class="parent">
    <div class="child">
        something here!
    </div>
</div>
```
            ''', inline=False)
            _embed.add_field(name='CSS', value='''
```css
.child {
    /* width of your choice */
    width: 50%
    margin: auto;
}
```
            ''', inline=False)
            await ctx.send(embed=_embed)
        # ! PRINT CENTER DIV TUTORIAL

        # ! PRINT COMPLETE BOX SHADOW TUTORIAL
        elif tutorial[0] == 'complete box shadow':
            _embed = discord.Embed(title=f'How to: `{tutorial[0]}`',
                                   description='Type `-tut` followed by a tutorial you want to see to display it!',
                                   color=0x1f8b4c)
            _embed.add_field(name='HTML', value='''
```html
<div class="shadow">
    Something here!
</div>
```
            ''', inline=False)
            _embed.add_field(name='CSS', value='''
```css
.shadow {
    /* box-shadow: h-position v-position blur color */
    box-shadow: 0 0 3px #ccc;
}
```
            ''', inline=False)
            await ctx.send(embed=_embed)
        # ! PRINT COMPLETE BOX SHADOW TUTORIAL
    ###################################################################################################################
    else:
        _embed = discord.Embed(title='More than one result found!',
                               description=f'More than one result have been found for the query `{arg}`.\nReact with the number of the tutorial you want to open.',
                               color=0x1f8b4c)
        i = 0
        for tutor in tutorial:
            i += 1
            embedText = f'{i} - `{tutor}`'
            _embed.add_field(name=embedText, value=f'React with `{i}` to choose this tutorial', inline=False)
        #          1     2     3    4     5
        emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
        message_choice = await ctx.send(embed=_embed)
        for x in range(i):
            await message_choice.add_reaction(emojis[x])
        time.sleep(1)
        # TODO display the tutorial the user has reacted to
        reaction, user = await bot.wait_for('reaction_add')


bot.run('ODIyNTMzMDY0NTE2ODI5MjA0.YFTpnA.BE8U2Micx7hlT8U5AKfTaStNbzE')
