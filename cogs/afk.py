import mysql.connector
import discord
from discord.ext import commands

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='password',  # パスワード
        host='localhost'  # ホスト名(IPアドレス）
    )
    if cnx.is_connected:
        print("Connected!")
except:
    pass

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx):
        # DB部分
        print('') #　仮のprint


async def setup(bot):
    await bot.add_cog(AFK(bot))
