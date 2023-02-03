import discord											
from discord.ext import commands						 
from discord_slash import SlashCommand, SlashContext	

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())	
slash = SlashCommand(bot)

@slash.slash(name="test")							
async def _test(ctx: SlashContext):					
    embed = discord.Embed(title="embed test")		
    await ctx.send(content="test", embeds=[embed])	

bot.run("discord_token")