from colorama import Back, Fore, Style
import os
import time
import platform
import asyncio
import subprocess
import discord
from discord import ui, app_commands
from discord.ext import commands
from datetime import datetime, timedelta

avatarbot = "https://media.discordapp.net/attachments/1173589548152926228/1201018181876199564/standard.gif"
Alert = "> ⚠️ คุณไม่มีสิทธิ์ หรือ การอนุณาติที่สามารถใช้คำสั่งนี้ได้คะ "
LOGCHANNEL = 1463520487249547386
TOKEN = os.getenv("DISCORD_TOKEN")
X = 50


# ---------- BUTTON ----------
class sms_button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="เริ่มการยิงเบอร์",
        style=discord.ButtonStyle.red,
        emoji="📨",
        custom_id="sms_button1"
    )
    async def sms_button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(MyModal())


# ---------- MODAL ----------
class MyModal(ui.Modal, title="ระบบยิงเบอร์ 98Api"):
    phone = ui.TextInput(label="ใส่เบอร์มือถือ 10 หลัก")
    amount = ui.TextInput(label="ใส่จำนวน (1-50)")

    async def on_submit(self, interaction: discord.Interaction):
        phone = self.phone.value
        amount_str = self.amount.value
        user = interaction.user

        if not amount_str.isdigit():
            await interaction.response.send_message("❌ จำนวนต้องเป็นตัวเลข", ephemeral=True)
            return

        amount = int(amount_str)
        if not 1 <= amount <= X:
            await interaction.response.send_message("❌ จำนวนต้องอยู่ระหว่าง 1-50", ephemeral=True)
            return

        # ตอบ interaction ครั้งแรก (สำคัญมาก)
        await interaction.response.send_message(
            f"✅ เริ่มยิงเบอร์ `{phone}` จำนวน `{amount}`",
            ephemeral=True
        )

        # เรียก sms.py
        subprocess.Popen([
            "python",
            "sms.py",
            phone,
            str(amount)
        ])

        # Embed แสดงสถานะให้ user
        embes = discord.Embed(
            title="สถานะการยิงเบอร์",
            color=0x15ff00
        )
        embes.add_field(name="เบอร์ 📵", value=f"`{phone}`", inline=False)
        embes.add_field(name="สถานะ 🧑‍🏫", value="กำลังทำงาน", inline=False)
        embes.add_field(name="จำนวน ⏱️", value=f"{amount}", inline=False)

        local_time = datetime.utcnow() + timedelta(hours=7)
        embes.timestamp = local_time
        embes.set_thumbnail(url=user.display_avatar.url)

        await interaction.followup.send(
            embed=embes,
            ephemeral=True
        )

        # LOG CHANNEL
        channel = interaction.client.get_channel(LOGCHANNEL)
        if channel:
            log_embed = discord.Embed(
                title="📳 แจ้งเตือนยิงเบอร์ SMS",
                description=(
                    f"👤 ผู้ใช้ : {user.mention}\n"
                    f"📱 เบอร์ : `{phone}`\n"
                    f"⏱️ จำนวน : `{amount}`"
                ),
                color=0x15ff00
            )
            log_embed.set_author(name="SMS SYSTEM", icon_url=avatarbot)
            log_embed.set_thumbnail(url=user.display_avatar.url)
            log_embed.timestamp = local_time

            msg = await channel.send(
                content="🟢 กำลังทำงาน",
                embed=log_embed
            )

            await asyncio.sleep(amount)
            await msg.edit(content="🔴 ทำงานเสร็จแล้ว", embed=log_embed)


# ---------- BOT ----------
class aclient(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('.'),
            intents=discord.Intents.all()
        )

    async def on_ready(self):
        prfx = (
            Back.BLACK + Fore.GREEN +
            time.strftime("%H:%M:%S UTC", time.gmtime()) +
            Back.RESET + Fore.WHITE + Style.BRIGHT
        )
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + platform.python_version())

        synced = await self.tree.sync()
        print(prfx + f" Slash CMDs Synced {len(synced)} Commands")

        self.add_view(sms_button())


client = aclient()


@client.tree.command(name="setupsms", description="สร้างเมนูยิงเบอร์")
async def setupsms(interaction: discord.Interaction):
    embed = discord.Embed(
        title="เมนูยิงเบอร์",
        description="กดปุ่มด้านล่างเพื่อเริ่มใช้งาน",
        color=0xff2c2c
    )
    embed.set_author(name=interaction.guild.name, icon_url=avatarbot)
    await interaction.channel.send(embed=embed, view=sms_button())


client.run(TOKEN)
