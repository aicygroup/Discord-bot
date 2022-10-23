import discord
from discord.ext import commands
from json import load, dumps


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def change_prefix(self, ctx, new_prefix: str):
        # コマンドが実行されたサーバーでカスタムprefixが設定されていれば実行
        if str(ctx.message.guild.id) in self.bot.prefix_json.keys():

            # dictからコマンドを実行したサーバーのカスタムprefix情報を削除
            self.bot.prefix_json.pop(str(ctx.message.guild.id))
            # dictにコマンドを実行したサーバーのカスタムprefix情報を追加
            self.bot.prefix_json[str(ctx.message.guild.id)] = new_prefix

            # jsonファイルにdict情報を記入
            with open('data/prefix.json', 'w', encoding='UTF-8') as f:
                f.write(dumps(self.bot.prefix_json))

            # 完了メッセージ
            await ctx.send(f'{ctx.message.guild.name} のprefixが{self.bot.prefix_json[str(ctx.message.guild.id)]}に変更されました')
            return

        else:
            # dictにコマンドを実行したサーバーのカスタムprefix情報を追加
            self.bot.prefix_json[str(ctx.message.guild.id)] = new_prefix

            # jsonファイルにdict情報を記入
            with open('data/prefix.json', 'w', encoding='UTF-8') as f:
                f.write(dumps(self.bot.prefix_json))

            # 完了メッセージ
            await ctx.send(f'{ctx.message.guild.name} のprefixが{self.bot.prefix_json[str(ctx.message.guild.id)]}に変更されました')
            return
async def setup(bot):
    await bot.add_cog(Bot(bot))
