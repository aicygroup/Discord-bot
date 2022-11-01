from cmath import e
import requests
import discord
import json
import asyncio
from discord.ext import commands



class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx, reason=None):
        await asyncio.sleep(1)
        url = requests.get(f'https://api.aic-group.net/get/afk?pass=ZxbOcHbVF9FEfoPbXq5QlQ2WcdnWmB6j&action=set&id={ctx.author.id}&name={ctx.author.name}&tag={ctx.author.discriminator}&reason={reason}')
        text = url.text
        data = json.loads(text)
        await self.bot.get_channel(1034783037029875729).send(data)
        if data['message'] == f'{ctx.author.id}をAFKしました。':
            e = discord.Embed(title='AFKに設定しました。', description='何か発言されたら、AFKを解除します。', timestamp=ctx.message.created_at, color=discord.Colour.from_rgb(160, 106, 84))
            await ctx.reply(embed=e)
        elif data['message'] == f'このユーザー({ctx.author.id})はすでにAFKです。':
            await ctx.reply('すでにAFKです。')
        elif data['message'] == f'このユーザー({ctx.author.id})はAFKではありません。':
            pass
        else:
            await ctx.reply('AFKをする際に、エラーが発生しました。後ほどお試しください。')
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in 'a.afk ':
            return
        if message.author.bot:
            return
        for m in message.mentions:
            user = self.bot.get_user(m.id)
            url = requests.get(f'https://api.aic-group.net/get/afk?pass={self.bot.afk_pass}&action=check&id={user.id}')
            text = url.text
            data = json.loads(text)
            await self.bot.get_channel(1034783037029875729).send(data)
            if data['message'] == f'このユーザー({user.id})はAFKです。':
                e = discord.Embed(title='このユーザーはAFKです。', description=data['reason']+'\n\n<t:'+data['time']+':R>からAFKです。', color=discord.Colour.from_rgb(160, 106, 84))
                e.set_footer(text='このメッセージは10秒後に削除されます。')
                msg = await message.reply(embed=e)
                await asyncio.sleep(11)
                await msg.delete()
            else:
                pass
        user = message.author
        url = requests.get(f'https://api.aic-group.net/get/afk?pass={self.bot.afk_pass}&action=check&id={user.id}')
        text = url.text
        data = json.loads(text)
        await self.bot.get_channel(1034783037029875729).send(data)
        if data['message'] == f'このユーザー({user.id})はAFKです。':
            url = requests.get(f'https://api.aic-group.net/get/afk?pass={self.bot.afk_pass}&action=unset&id={user.id}')
            text = url.text
            data = json.loads(text)
            await self.bot.get_channel(1034783037029875729).send(data)
            em = discord.Embed(title='AFK解除', description='AFKを解除しました。', color=discord.Colour.from_rgb(160, 106, 84))
            em.set_footer(text='このメッセージは5秒後に削除されます。')
            msg=await message.reply(embed=em)
            await asyncio.sleep(6)
            await msg.delete()
        else:
            pass


async def setup(bot):
    await bot.add_cog(AFK(bot))
