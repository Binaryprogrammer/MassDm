import discord

# Enter your bot token here
TOKEN = 'MTIyNDgwODU2NjA0NTY3NTYxMA.GCCUJ8.H16fmwxefDopJUztpTtLzaX9hpJmM5qbBUA8gI'

# Message to send
message = "Enter the message you want the bot to send here"


intents = discord.Intents.default()
intents.members = True  


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')

    # List of guild IDs where you want to send the message
    guild_ids = ['1224810335781785682',]  # Add more guild IDs as needed

    
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
