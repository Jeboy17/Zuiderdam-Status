import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ Online als {client.user}")

@tree.command(name="ping", description="Check of de bot online is")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

client.run(TOKEN)
