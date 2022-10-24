from asyncio import events
import discord
from discord.ext import commands
from discord.ext.commands import errors
import traceback


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_ch = self.bot.get_channel(1034092748078334093)
        if isinstance(error, errors.MissingPermissions):
            embed = discord.Embed(title=":x: 失敗 -MissingPermissions", description=f"実行者の必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        elif isinstance(error, errors.BotMissingPermissions):
            embed = discord.Embed(title=":x: 失敗 -BotMissingPermissions", description=f"Botの必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        elif isinstance(error, errors.CommandNotFound):
            embed = discord.Embed(title=":x: 失敗 -CommandNotFound", description=f"不明なコマンドもしくは現在使用不可能なコマンドです。", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        elif isinstance(error, errors.MemberNotFound):
            embed = discord.Embed(title=":x: 失敗 -MemberNotFound", description=f"指定されたメンバーが見つかりません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        elif isinstance(error, errors.BadArgument):
            embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        elif isinstance(error, errors.MissingRequiredArgument):
            embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数が足りないため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":x: 失敗 - Unknown error", description=f"不明なエラーが発生しました。\nお問い合わせの際はこちらのコードも一緒にお持ちください。{ctx.message.id}", timestamp=ctx.message.created_at, color=discord.Colour.red())
            embed.set_footer(text="お困りの場合は、サポートサーバーまで質問をお願いします。")
            await ctx.send(embed=embed)
        e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
        e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
        e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
        e.add_field(name='エラーid', value=ctx.message.id, inline=False)
        e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
        e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
        e.add_field(name='エラー内容', value=error, inline=False)
        await error_ch.send(embed=e)
        orig_error = getattr(error, "original", error)
        error_msg  = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        await error_ch.send('エラー全文')
        await error_ch.send(error_msg)
async def setup(bot):
    await bot.add_cog(Error(bot))
