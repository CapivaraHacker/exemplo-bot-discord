# Importações
import discord
from discord.ext import commands

# Intents e criação do bot
intents = discord.Intents.all() # Ativa todas as intents
bot = commands.Bot('!', intents=intents)


# Comando "!olá"
@bot.command(aliases=["echo", "oi"])
async def olá(ctx): # Cria a função assíncrona
    autor = ctx.author.mention # Menção do autor
    await ctx.send(f'Olá, {autor}!') # Envia uma mensagem

bot.run('MTE1NzgxMzA1NDI2MDY1MDAwNA.GIAtQw.GUucsVmaMHgCNw7quMx683vlxBFnsw6Y7Eu6zU') # Roda o bot
