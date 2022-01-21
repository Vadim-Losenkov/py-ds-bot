async def permissions_error(ctx):
  author = ctx.message.author
  await ctx.send(f'{author.mention}, эту комманду могут использовать только админы!')
