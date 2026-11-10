from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token and openrouter key from environment variables
bot_token = os.getenv("BOT_TOKEN")
openrouter_key = os.getenv("OPENROUTER_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_key,
)


def call_openrouter(prompt):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user", 
                "content": f"Respond with sarcasm: {prompt}"
            }
        ]
    )

    # Print the response
    print(response.choices[0].message.content)
    return response.choices[0].message.content

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

    if message.content.startswith('!ask'):
        print(f"Message: {message.content}")
        message_content = message.content[len('!ask'):].strip()
        print(f"Message content: {message_content}")
        response = call_openrouter(message_content)
        print(f"Response: {response}")
        print("------")
        await message.channel.send(response)

# Run the bot
bot.run(bot_token)