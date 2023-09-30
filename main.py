import discord, random, os, asyncio, keep_alive
from discord.ext import commands

paused = False
spam_id = os.environ['spam_id']
client, token = commands.Bot(command_prefix='!', help_command=None), os.environ['token']

class ChannelNotFound(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message

async def spam(canal, time):
    if canal:
        while True:
            try:
                if not paused:
                    await canal.send(''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 7) * 4))
                await asyncio.sleep(random.choice(time))
            except:
                await asyncio.sleep(60)
                pass
    else:
        raise ChannelNotFound('Canal Nao Encontrado Verifique seu "spam_id".')
    

@client.event
async def on_ready():
    print('Logado em {0}'.format(client.user.name))
    canal = client.get_channel(int(spam_id))
    await spam(canal, [3.5, 3.4, 2, 5, 4.3])

@client.event
async def on_message(message):
    if not message.author.bot and str(message.channel.id) == str(spam_id):
        await client.process_commands(message)



@client.command(name='stop', aliases=['pause'])
async def stop(ctx):
    if not str(ctx.channel.id) == str(spam_id):
        return
    global paused
    if not paused:
        paused = True
        await ctx.send('Bot pausado')
    else:
        await ctx.send('bot ja esta pausado')

@client.command(name='start', aliases=['unpause'])
async def start(ctx):
    if not str(ctx.channel.id) == str(spam_id):
        return
    global paused
    if paused:
        paused = False
        await ctx.send('bot despausado')
    else:
        await ctx.send('bot ja esta em execuçao')


keep_alive.keep_alive()
client.run(token)
