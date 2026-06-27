import asyncio
import os
import discord
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Initialize the bot client with permissions
intents = discord.Intents(members=True, voice_states=True)
client = discord.Client(intents=intents)

# 3. The updated looping logic with Discord messages
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    
    GUILD_ID = 822516568662868089
    TEXT_CHANNEL_ID = 123456789012345678  # 👈 PASTE YOUR COPIED TEXT CHANNEL ID HERE
    
    guild = client.get_guild(GUILD_ID)
    channel = client.get_channel(TEXT_CHANNEL_ID)
    
    if guild is None:
        print("Guild not found. Check your GUILD_ID.")
        return
    if channel is None:
        print("Text channel not found. Check your TEXT_CHANNEL_ID and bot permissions.")
        return

    # This loop runs forever while the bot is online
    while True:
        print("Checking user status...")
        
        # Fetch the member from the guild
        member = guild.get_guild(GUILD_ID).get_member(750142815811534889)

        if member and member.voice is not None:
            print("User is in a voice channel. Printing to terminal.")
            # Optional: You can also have the bot send a message saying they joined
            # await channel.send("moobs on")
        else:
            print("User missing from voice. Sending Discord message.")
            # This sends an actual message tagging the user ID
            await channel.send("<@750142815811534889> wake up!")

        # Wait 60 seconds before checking again
        await asyncio.sleep(60)

# 4. Run the bot
client.run(os.getenv('DISCORD_TOKEN'))