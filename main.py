import discord

client = discord.Client()

@client.event
async def on_ready():
  print(str(client.user) + ' is going for it!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  messagecon = message.content.lower()
  if messagecon.startswith('heyo'):
    await message.channel.send('Heyooo! Suuup!')

client.run(process.env.BOT_TOKEN)