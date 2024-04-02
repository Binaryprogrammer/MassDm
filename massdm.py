import discord

# Enter your bot token here
TOKEN = 'your_bot_token_here'

# Message to send
message = "Hey everyone! This is a mass DM from your friendly neighborhood hacker. Enjoy!"

# Define intents
intents = discord.Intents.default()
intents.members = True  # Enable the members intent

# Initialize the client with intents
client = discord.Client(intents=intents)

# Event for when the bot is ready
@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')

    # List of guild IDs where you want to send the message
    guild_ids = ['guild_id_1', 'guild_id_2', 'guild_id_3']  # Add more guild IDs as needed

    # Iterate over guild IDs
    for guild_id in guild_ids:
        guild = client.get_guild(int(guild_id))
        if guild:
            print(f'Sending message to members in server with ID: {guild_id}')

            # Iterate over all members in the guild and send message
            for member in guild.members:
                try:
                    await member.send(message)
                    print(f"Message sent to {member.name}#{member.discriminator}")
                except Exception as e:
                    print(f"Failed to send message to {member.name}#{member.discriminator}: {e}")
        else:
            print(f"Guild with ID {guild_id} not found.")

# Run the bot
client.run(TOKEN)
