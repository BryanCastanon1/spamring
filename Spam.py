import asyncio
import os
import discord
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Initialize the bot client with permissions
intents = discord.Intents(members=True, voice_states=True)
client = discord.Client(intents=intents)

# 3. The updated looping logic
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    
    GUILD_ID = 822516568662868089
    guild = client.get_guild(GUILD_ID)
    
    if guild is None:
        print("Guild not found. Make sure the ID is correct and the bot is in the server.")
        return

    # This loop runs forever while the bot is online
    while True:
        print("Checking user status...")
        
        # Fetch the member from the guild (using your target user ID)
        member = guild.get_member(750142815811534889)

        if member and member.voice is not None:
            print("moobs on")
        else:
            print("@accepted.bot - User is not in a voice channel.")
            # Note: Right now this just prints to your terminal. 
            # If you want it to send a real message to a Discord channel, let me know!

        # Wait 60 seconds before looping back up to check again
        await asyncio.sleep(60)

# 4. Run the bot using your .env token
client.run(os.getenv('DISCORD_TOKEN'))