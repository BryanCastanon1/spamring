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
    if guild is None:
        print("Guild not found. Check your GUILD_ID.")
        return

    # Force a direct API fetch from Discord instead of checking the empty cache
    try:
        channel = await client.fetch_channel(TEXT_CHANNEL_ID)
        print(f"Successfully connected to channel: #{channel.name}")
    except Exception as e:
        print(f"Failed to fetch channel: {e}")
        print("Please double-check your bot permissions and the TEXT_CHANNEL_ID.")
        return

    # This loop runs forever while the bot is online
    while True:
        print("Checking user status...")
        
        # Pull the fresh member object from the guild
        member = guild.get_member(750142815811534889)

        if member and member.voice is not None:
            print("User is in a voice channel. Printing to terminal.")
        else:
            print("User missing from voice. Sending Discord message.")
            try:
                await channel.send("<@750142815811534889> wake up!")
            except Exception as e:
                print(f"Could not send message: {e}")

        # Wait 60 seconds before checking again
        await asyncio.sleep(60)
# 4. Run the bot
client.run(os.getenv('DISCORD_TOKEN'))