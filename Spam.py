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
    TEXT_CHANNEL_ID = 822516568662868092  # Ensure this is a TEXT channel ID
    
    guild = client.get_guild(GUILD_ID)
    
    print("Available channels:", [c.name for c in guild.text_channels])
    print("Available IDs:", [c.id for c in guild.text_channels])
    
    if guild is None:
        print("Guild not found. Check your GUILD_ID.")
        return

    # Look for the channel inside this specific guild
    channel = guild.get_channel(TEXT_CHANNEL_ID)
    
    if channel is None:
        print("Text channel not found. Check your TEXT_CHANNEL_ID and bot permissions.")
        return

    # This loop runs forever while the bot is online
    while True:
        print("Checking user status...")
        
        # Pull the fresh member object from your guild cache
        member = guild.get_member(750142815811534889)

        if member and member.voice is not None:
            print("User is in a voice channel. Printing to terminal.")
        else:
            print("User missing from voice. Sending Discord message.")
            # This sends an actual message tagging the user ID in chat
            await channel.send("<@750142815811534889> wake up!")

        # Wait 60 seconds before checking again
        await asyncio.sleep(60)

# 4. Run the bot
client.run(os.getenv('DISCORD_TOKEN'))