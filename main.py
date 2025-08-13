import os
import discord
from discord.ext import commands

TOKEN = os.getenv("BOT_TOKEN")
WELCOME_CHANNEL_ID = 1401230000249766008  # 환영 채널 ID

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 봇 로그인 성공: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            description=(
                f"✨ {member.mention} 환영합니다!\n\n"
                f"**<#1398259715192127569> 인증 하시면 활동 가능합니다.**\n"
                f"**<#1398260667768635392> 서버 이용 전 꼭 필독해주세요.**"
            ),
            color=discord.Color(0x000000)
        )
        embed.set_footer(text="서버에 오신 걸 환영합니다!")
        await channel.send(embed=embed)

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN 환경변수가 설정되지 않았습니다!")

bot.run(TOKEN)
