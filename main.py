import discord
from discord.ext import commands

# Set up the bot with the command prefix
bot = commands.Bot(command_prefix='!')

# Event to detect new member join
@bot.event
async def on_member_join(member):
    print(f'{member.name} has joined the server.')
    # Example raid protection feature: limit new members
    guild = member.guild
    if len(guild.members) > 50:  # adjust this number based on your needs
        await member.kick(reason='Raid protection triggered: too many new members joined.')
        print(f'Kicked {member.name} to prevent raid.')

# Command to check bot status
@bot.command()
async def status(ctx):
    await ctx.send('Bot is online and functioning!')

# Run the bot with your token
TOKEN = 'YOUR_BOT_TOKEN'
bot.run(TOKEN)