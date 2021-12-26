import discord.ext


class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = DiscordClient()
client.run('jg2tXqJWD2N4eI8ZG29Td5zpw69MiPo7')
