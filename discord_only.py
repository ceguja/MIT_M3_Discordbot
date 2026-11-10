from dotenv import load_dotenv
import discord
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
bot_token = os.getenv("BOT_TOKEN")

# Create a Discord bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# Define a simple event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Run the bot
bot.run(bot_token)