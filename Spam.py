import asyncio
import os
import discord
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Initialize the bot client with permissions (This removes the yellow lines!)
intents = discord.Intents(members=True, voice_states=True)
client = discord.Client(intents=intents)

# 3. Put your logic inside an async event
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    
    GUILD_ID = 822516568662868089
    guild = client.get_guild(GUILD_ID)
    
    if guild is None:
        print("Guild not found. Make sure the ID is correct and the bot is in the server.")
        return

    print("Waiting for user to join...")
    await asyncio.sleep(10)  # Wait 10 seconds

    # Fetch the member from the guild (using your target user ID)
    member = guild.get_member(750142815811534889)

    if member and member.voice is not None:
        print("moobs on")
    else:
        print("@accepted.bot")
        # send reminder message here

# 4. Run the bot using your .env token
client.run(os.getenv('DISCORD_TOKEN'))