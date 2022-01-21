import config
from kazino import getRunCfc
from utils import permissions_error

import discord 
from discord.ext import commands
from discord import utils

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=config.BOT_PREFIX)
client.remove_command('help')

# слушаем события сообщений на сервере
@client.event
async def on_message(message):
  msg = message.content.lower()
  # если в сообщении есть слово из массива слов
  # бот пишет в чат
  if msg in kazino_words:
    cfc = getRunCfc()
    
    emb = discord.Embed(title='Последние 30 коэффициэнтов на csgorun.gg', colour=discord.Color.blue())
    emb.set_author(name='csgorun.gg', icon_url='https://yandex.ru/images/touch/search?pos=2&img_url=https%3A%2F%2Fsun9-23.userapi.com%2Fimpg%2FTcssqdPHwiW8SigE6cn1iCNVJOGydfG9H_7Xuw%2F5aBvUmHnC-4.jpg%3Fsize%3D604x604%26quality%3D96%26sign%3D280c4fa46c0207a35a11b6cb9ca16165%26type%3Dalbum&text=csgorun&rpt=simage&source=tabbar')
    
    emb.set_footer(text=getRunCfc())
    
    await message.channel.send(embed=emb)
  else: 
    await client.process_commands(message)

# слова казик
kazino_words = [
  'краш',
  'ран',
  'кфы',
  'казик'
]

@client.event
async def on_ready(): 
  print('BOT connected')

# test command
@client.command(name='hi', aliases=['hello'])
async def _hi(ctx):
  author = ctx.message.author
  await ctx.send(f'Hello {author.mention}! DS bot working!')

# echo
@client.command()
async def echo(ctx, msg):
  author = ctx.message.author
  await ctx.send(f'{author} say: \'{msg}\'')
  
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
  await ctx.channel.purge(limit=amount)
  
  author = ctx.message.author
  await ctx.send(f'Админ {author.mention} очистил чат.\n\nУдалено {amount} Сообщений!')

@client.command()
async def help(ctx):
  emb = discord.Embed(title='Комманды Бота', colour=discord.Color.green())
  
  emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
  
  emb.add_field(name=f'{config.BOT_PREFIX}clear', value='Очистит последние 100 сообщений чата, или столько, сколько было указано в параметре\n')
  
  emb.add_field(name=f'[Ран, Краш, Кфы, Казик]', value='показывает последние 30 коэфов на csgorun\n')
  emb.add_field(name=f'{config.BOT_PREFIX}hi', value='Проверка бота\n')
  emb.add_field(name=f'{config.BOT_PREFIX}echo', value='Повторяет за тобой текст укащанный в параметре\n')
  
  emb.set_footer(text='footer_text', icon_url=ctx.author.avatar_url)
  
  await ctx.send(embed=emb)
  
@clear.error
async def clear_error(ctx, error):
  author = ctx.message.author
  await ctx.send(f'{author.mention}, эту комманду могут использовать только админы!')


client.run(config.TOKEN)