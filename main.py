# Importações
import discord
from discord.ext import commands

# Intents e criação do bot
intents = discord.Intents.all()
bot = commands.Bot('!', intents=intents)


# Comando "!olá"

@bot.command(aliases=["echo", "oi"])
async def olá(ctx):
    autor = ctx.author.mention
    await ctx.send(f'Olá, {autor}!')

bot.run('MTE1NzgxMzA1NDI2MDY1MDAwNA.GIAtQw.GUucsVmaMHgCNw7quMx683vlxBFnsw6Y7Eu6zU')