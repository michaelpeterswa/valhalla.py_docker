import discord, datetime, time
from discord.ext import commands
import random
import credentials

TOKEN = credentials.apikey

bot = commands.Bot(command_prefix='v ', description="valhalla")

start_time = time.time()

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print(discord.utils.oauth_url(bot.user.id))
	await bot.change_presence(game=discord.Game(name='v help | '+ str(len(bot.servers)) +' | nwradio#2779'))

@bot.command()
async def guildcount():
	"""Bot Guild Count"""
	await bot.say("**I'm in {} Guilds!**".format(len(bot.servers)))

@bot.command()
async def invite():
	"""Bot Invite"""
	await bot.say("\U0001f44d")
	await bot.whisper("Add me with this link {}".format(discord.utils.oauth_url(bot.user.id)))

@bot.command(pass_context=True)
async def roll(ctx, *, val):
	"""Rolls a dice of n sides (v roll n)"""
	embed = discord.Embed(title="Current roll (" + val + "-sided) is:", description="🎲 " + str(random.randint(1,int(val))) + " 🎲", color=0xff0000)
	await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def kickornah(ctx):
	"""Decides whether to kick person or not"""
	randNum = random.randint(0,1)
	if randNum == 0:
		embed = discord.Embed(title="The verdict is in:", description="Nah. You have been spared", color=0x00ff00)
		await bot.send_message(ctx.message.channel, embed=embed)
	if randNum == 1:
		embed = discord.Embed(title="The verdict is in:", description="Kick. The decision is final", color=0xff0000)
		await bot.send_message(ctx.message.channel, embed=embed)

@bot.event
async def on_message(message):
	if not (message.author).bot:
		if message.content.startswith('v '):
			await bot.delete_message(message)
	await bot.process_commands(message)

@bot.command(pass_context=True)
async def uptime(ctx):
	"""Returns uptime"""
	current_time = time.time()
	difference = int(round(current_time - start_time))
	text = str(datetime.timedelta(seconds=difference))
	embed = discord.Embed(colour=ctx.message.author.top_role.colour)
	embed.add_field(name="Uptime", value=text)
	embed.set_footer(text="sponsored by nwradio#2779 | ran on RPi3")
	try:
		await bot.send_message(ctx.message.channel, embed=embed)
	except discord.HTTPException:
		await bot.say("Current uptime: " + text)


def is_me(m):
    return m.author == bot.user

@bot.command(pass_context=True)
async def clear(ctx):
	"""Clears messages from bot"""
	deleted = await bot.purge_from(ctx.message.channel, limit=100, check=is_me)
	await bot.send_message(ctx.message.channel, 'Deleted {} message(s)'.format(len(deleted)))



bot.run(TOKEN)
