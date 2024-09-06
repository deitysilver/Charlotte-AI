import discord
import requests
import json

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
        data = {
            "model": model,
            "prompt": message.content,
        }
        response = requests.post(url, json=data)
        response_text = response.text

        response_lines = response_text.splitlines()
        response_json = [json.loads(line) for line in response_lines]

        finalMessage = ""
        for line in response_json:
            print(line["response"], end="")
            finalMessage = finalMessage + line["response"]


        await message.channel.send(finalMessage)

client.run(TOKEN)
