import discord
import ollama

TOKEN = ""
url = "http://localhost:11434/api/generate"
model = "gurubot/tinystories-656k-q8:latest"

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Charlotte is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        finalMessage = ollama.generate(model=model, prompt='Why is the sky blue?')

        await message.channel.send(finalMessage["response"])

client.run(TOKEN)
