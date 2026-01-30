from colorama import Back, Fore, Style
import os
import json
from requests import post, Session, get
from random import choice
import random
import threading
from discord.ext import commands
import requests as ru
import discord
from discord import ui
import time
import platform
from datetime import datetime
import pytz
import asyncio
import socket
from discord import app_commands
from discord.ext.commands import Bot
import aiohttp
import uuid
from typing import Literal
import json
from bs4 import BeautifulSoup as bs
from pystyle import Colors, Colorate
import itertools
from discord import SyncWebhook
import requests
from re import match
import sys
import subprocess
from discord import Activity, ActivityType, Status
from datetime import datetime, timedelta
import datetime


avatarbot = "https://media.discordapp.net/attachments/1173589548152926228/1201018181876199564/standard.gif?ex=65c84a58&is=65b5d558&hm=a90543158db13e39ff1c70b303ff4d9bc12367e51c437e54969af80d4c6c2979&=&width=288&height=288"
Alert = "> ⚠️ คุณไม่มีสิทธิ์ หรือ การอนุณาติที่สามารถใช้คำสั่งนี้ได้คะ "

LOGCHANNEL = 1463520487249547386
TOKEN = os.getenv("DISCORD_TOKEN")

X = 50 # จำนวนทั้งหมด
class sms_button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="เริ่มการยิงเบอร์", style=discord.ButtonStyle.red, emoji="<:DG16:1184837310492197004> ", custom_id="sms_button1")
    async def sms_button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(MyModal())



class MyModal(ui.Modal, title="ระบบยิงเบอร์ 98Api"):
    phone = ui.TextInput(label="ใส่เบอร์มือถือ 10 หลัก", placeholder="062xxxxxxx", style=discord.TextStyle.short)
    amount = ui.TextInput(label="ใส่จำนวน", placeholder="จำนวนที่ต้องการยิง", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        phone = self.phone.value
        amount_str = self.amount.value
        user = interaction.user

    if not amount_str.isdigit():
        await interaction.response.send_message(
            "กรุณาใส่ตัวเลขเท่านั้น",
            ephemeral=True
        )
        return

    amount = int(amount_str)

    if not 1 <= amount <= X:
        await interaction.response.send_message(
            "จำนวนที่ต้องการยิงต้องอยู่ในช่วง 1-50",
            ephemeral=True
        )
        return

    embes = discord.Embed(
        title="สถานะการยิงเบอร์",
        description="",
        color=0x15ff00
    )

    embes.add_field(
        name="",
        value=f"```เบอร์ 📵: {phone}```",
        inline=False
    )
    embes.add_field(
        name="",
        value="```สถานะ 🧑‍🏫 : สุ่ม```",
        inline=False
    )
    embes.add_field(
        name="",
        value=f"```เวลา 🗃️ : {amount} นาที```",
        inline=False
    )

    current_time = datetime.datetime.utcnow()
    local_time = current_time + datetime.timedelta(hours=7)

    embes.timestamp = local_time
    embes.set_thumbnail(url=user.avatar.url)
    embes.set_image(
        url="https://media1.giphy.com/media/xFBnkMvpTM6m4/giphy.gif"
    )

    await interaction.response.send_message(
        content=interaction.user.mention,
        embed=embes,
        ephemeral=True
    )

    channel = client.get_channel(LOGCHANNEL)
    if channel is None:
        await interaction.followup.send(
            "❌ ไม่พบห้อง LOGCHANNEL",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="📳 แจ้งเตือนยิงเบอร์ SMS",
        description=(
            f"\n👤 ผู้ใช้งาน : {interaction.user.mention}"
            f"\n\n📱 เบอร์ที่ยิง : {phone}"
            f"\n\n↗️ เวลา : {amount} นาที"
        ),
        color=0x15ff00
    )

    embed.set_author(
        name="SMS FLOOD 220API",
        icon_url=avatarbot
    )
    embed.set_thumbnail(url=user.avatar.url)
    embed.timestamp = local_time

    message1 = await channel.send(
        content="**🟢 : สถานะกำลังยิงเบอร์**",
        embed=embed
    )

    try:
        subprocess.Popen(
            ["python", "sms.py", phone, str(amount)]
        )
        await asyncio.sleep(amount)
        await message1.edit(
            content="**🔴 สถานะยิงเบอร์หมดแล้ว (ถึงเวลาที่กำหนดแล้ว)**",
            embed=embed
        )
    except Exception as e:
        print(f"Error in apiXaicas_ice: {e}")


        current_time = datetime.datetime.utcnow()
        local_time = current_time + datetime.timedelta(hours=7)
        embes.timestamp = local_time
        embes.set_thumbnail(url=user.avatar.url)
        embes.set_image(url="https://media1.giphy.com/media/xFBnkMvpTM6m4/giphy.gif?cid=ecf05e47hghqlrhpbvgv0j5objsdq2hbltz1y23cq75nhdov&ep=v1_gifs_search&rid=giphy.gif&ct=g")

        await interaction.response.send_message(content=f"{interaction.user.mention}", embed=embes, ephemeral=True)

        channel = client.get_channel(LOGCHANNEL)
        embed = discord.Embed(title="📳 แจ้งเตือนยิงเบอร์ SMS ", description=f"\n👤 ผู้ใช้งาน : {interaction.user.mention} \n\n📱 เบอร์ที่ยิง : {phone}\n\n↗️ เวลา : {amount} นาที", color=0x15ff00)
        embed.set_author(name="SMS FLOOD 220API", url="", icon_url=avatarbot)   
        embed.set_thumbnail(url=user.avatar.url)
        embed.timestamp = local_time
        embed.set_image(url="https://media.discordapp.net/attachments/1187996016591507477/1191739199251021914/standard_2.gif?ex=65a6889e&is=6594139e&hm=102d9d8f299911e079dacaa481cc87c3f9e84baba0b3c065448ee8c4853d7769&=&width=585&height=75")

        message1 = await channel.send(content="**🟢 : สถานะกำลังยิงเบอร์  **", embed=embed)
        try:
            process = subprocess.Popen(["python", "sms.py", phone, amount])
            await asyncio.sleep(amount)
            await message1.edit(content="**🔴 สถานะยิงเบอร์หมดแล้ว (ถึงเวลาที่กำหนดแล้ว)**", embed=embed)
        except Exception as e:
            print(f"Error in apiXaicas_ice: {e}")





class aclient(commands.Bot):    
    def __init__(self): 
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())
        self.role = None

    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        activity = discord.Streaming(name="24Hr Online", url="https://www.twitch.tv/yanglarkdeveloper")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) + " Commands")
        self.add_view(sms_button())



client = aclient()
@client.tree.command(name='setupsms', description='adminonly・สร้างยิงเบอร์')

async def setupsms(interaction: discord.Interaction):
      embed=discord.Embed(title="เมนูยิงเบอร์ทั่วไป", description="`🎆` `:` กดปุ่มเพื่อใช้งานได้เลยครับ", color=0xff2c2c)
      embed.add_field(name="", value="```diff\n-  อย่ากดมากเกินไปเพราะบอททำงานได้ ต่อคนเท่านั้น \n```", inline=True)
      embed.set_author(name=f"{interaction.guild.name}", url="", icon_url=avatarbot)
      embed.set_image(url="https://media.discordapp.net/attachments/1279497810198269964/1287795929549766677/IMG_0423.gif?ex=66ff5f2b&is=66fe0dab&hm=6fb64a661d87153c3092d833d999c31652ea856ebab1bae8d6781785bbc7e067&=&width=699&height=349")
      await interaction.channel.send(embed=embed,view=sms_button())
@setupsms.error
async def setupsms(interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingPermissions):
            await interaction.response.send_message(f"{Alert}", ephemeral=True)





client.run(TOKEN)



