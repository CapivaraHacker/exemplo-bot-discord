# Importações
import discord
from discord.ext import commands

# Intents e criação do bot
intents = discord.Intents.all() # Ativa todas as intents
bot = commands.Bot('[SEU PREFIXO]', intents=intents)


# Comando "!olá"
@bot.command(aliases=["echo", "oi"])
async def olá(ctx): # Cria a função assíncrona
    autor = ctx.author.mention # Menção do autor
    await ctx.send(f'Olá, {autor}!') # Envia uma mensagem

bot.run('[SEU TOKEN]') # Roda o bot
