import discord
from discord.ext import commands, tasks
from json import load, dumps
import traceback
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')
BACKUP_CHANNEL_ID = 1033503818765320232
DEFAULT_PREFIX = 'a.'

def custom_prefix(bot: commands.Bot, msg: discord.Message):
    with open('./data/prefix.json', encoding='UTF-8') as f:
            prefix_json = load(f)
        # コマンドが実行されたサーバーでカスタムprefixが設定されていれば対応するprefixを返す
    if str(msg.guild.id) in prefix_json.keys():
        return prefix_json[str(msg.guild.id)]
    # コマンドが実行されたサーバーでカスタムprefixが設定されていなければデフォルトprefixを返す
    else:
        return DEFAULT_PREFIX

class Aicybot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=custom_prefix,
            allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False),
            intents=discord.Intents.all()
        )
        self.afk_pass = os.getenv('afk-pass')
        self.admin_guild = bot.get_guild(1033496363897475163)
        self.owner = bot.get_user(964887498436276305)
    async def on_ready(self):
        await bot.change_presence(activity = discord.Activity(name=f"起動中", type=discord.ActivityType.playing), status='dnd')
        print('Loading any items')
        #prefix json loader
        try:
            with open('./data/prefix.json', encoding='UTF-8') as f:
                bot.prefix_json = load(f)
            print('Prefixes loaded')
        except:
            traceback.print_exc()
        #config loader
        try:
            with open('./data/config.json', 'r+', encoding='utf-8') as file:
                bot.config = load(file)
            print('Config loaded')
        except:
            traceback.print_exc()
        #jishaku loader
        try:
            await bot.load_extension("jishaku")
            print("Loaded jishaku")
        except:
            traceback.print_exc()
        # cog loader
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                try:
                    await bot.load_extension(f'cogs.{file[:-3]}')
                    print(f'Loaded cog: {file[:-3]}')
                except:
                    traceback.print_exc()
        await bot.change_presence(activity = discord.Activity(name='起動したよ Ver:β', type=discord.ActivityType.playing), status='online')
        print(f'Logged in {bot.user}')
        
        await bot.get_channel(1034784718123704361).send(embed=discord.Embed(title='起動完了', description=f'サーバー数:{len(bot.guilds)}\nメンバー数：{len(bot.users)}'))


bot=Aicybot()


bot.run(token)