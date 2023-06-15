import discord
import responses
from discord.ext import commands, tasks


async def send_message(message, user_message, is_private):
	try:
		response = responses.get_response(user_message)
		await message.author.send(response) if is_private else await message.channel.send(response)

	except Exception as e:
		print(e)

def read_token() -> str:
	with open("TOKEN.txt", 'r') as token_file:
		return token_file.read()

def run_discord_bot():
	TOKEN = read_token()
	intents = discord.Intents.default()
	intents.message_content = True
	client = discord.Client(intents=intents)

	
	@tasks.loop(seconds=1)
	async def loop():
		print("I'm running!")
		# your repetitive task


	@client.event
	async def on_ready():
		print(f'{client.user} is now running!')
		if not loop.is_running():
			loop.start()


	@client.event
	async def on_message(message):
		if message.author == client.user:
			return

		username = str(message.author)
		user_message = str(message.content)
		channel = str(message.channel)

		print(f'{username} said: "{user_message}" ({channel})')

		if user_message[0] == '?':
			user_message = user_message[1:]
			await send_message(message, user_message, is_private=True)
		else:
			await send_message(message, user_message, is_private=False)

	client.run(TOKEN)
