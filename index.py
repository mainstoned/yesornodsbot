import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '/')

token = open("token.txt", "r").readline()



@client.event
async def on_ready():

	streaming = discord.Streaming(type = 1, url = 'https://twitch.tv/yesorno72438762438723', name = 'Да или Нет?')

	await client.change_presence(status = discord.Status.idle, activity = streaming)

	print('Бот запущен!')

@client.command(aliases = ['шар', 'ball', 'магшар', 'magicball', '8ball'])
async def yon(ctx, *, question = None):

	if question is None:

		await ctx.send('Укажи вопрос!')

		return

	else:
		answers = [
		'Да, будь уверен в этом',
		'Возможно',
		'Скорее да, чем нет :eyes:',
		'Скорее нет, чем да :eyes:',
		'Сомневаюсь в этом',
		'Нет, точно',
		'Да',
		'Нет',
		'Тони трап!!!'
		]

		answer = random.choice(answers)

		await ctx.send(f'{answer}')

client.run(token)