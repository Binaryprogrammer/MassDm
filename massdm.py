import discord

# Enter your bot token here
TOKEN = 'your_bot_token_here'

# Message to send
message = "your message here"


intents = discord.Intents.default()
intents.members = True  # Enable the members intent


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')

   
    guild_ids = ['guild_id_1', 'guild_id_2', 'guild_id_3']  # Add more guild IDs as needed

    
    for guild_id in guild_ids:
        guild = client.get_guild(int(guild_id))
        if guild:
            print(f'Sending message to members in server with ID: {guild_id}')

            
            for member in guild.members:
                try:
                    await member.send(message)
                    print(f"Message sent to {member.name}#{member.discriminator}")
                except Exception as e:
                    print(f"Failed to send message to {member.name}#{member.discriminator}: {e}")
        else:
            print(f"Guild with ID {guild_id} not found.")

client.run(TOKEN)
