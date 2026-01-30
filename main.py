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
from flask import Flask, request, redirect, url_for, render_template_string
import subprocess
import uuid
import time
import threading

app = Flask(__name__)

X = 50  # จำกัดจำนวนเหมือนเดิม

# เก็บงานทั้งหมดไว้ใน RAM
JOBS = {}
# JOBS[job_id] = {
#   "phone": "...",
#   "amount": int(minutes),
#   "start_time": float,
#   "end_time": float,
#   "status": "running" / "done" / "error",
#   "error": ""
# }

INDEX_HTML = """
<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ระบบยิงเบอร์ 98Api</title>
  <style>
    body{font-family:sans-serif;background:#0b0f19;color:#fff;display:flex;justify-content:center;padding:30px}
    .card{width:100%;max-width:520px;background:#121a2b;border-radius:16px;padding:22px;box-shadow:0 10px 30px rgba(0,0,0,.4)}
    h1{margin:0 0 14px;font-size:22px}
    label{display:block;margin-top:12px;margin-bottom:6px;color:#cbd5e1}
    input{width:100%;padding:12px;border-radius:12px;border:1px solid #2a3552;background:#0b1220;color:#fff;font-size:16px}
    button{margin-top:16px;width:100%;padding:12px;border:0;border-radius:12px;background:#ff2c2c;color:#fff;font-size:16px;font-weight:700;cursor:pointer}
    .msg{margin-top:14px;padding:12px;border-radius:12px}
    .ok{background:#12351e;border:1px solid #2bd576}
    .err{background:#3a1111;border:1px solid #ff4d4d}
    .note{margin-top:12px;color:#94a3b8;font-size:13px}
  </style>
</head>
<body>
  <div class="card">
    <h1>ระบบยิงเบอร์ 98Api</h1>

    <form method="post" action="/send">
      <label>ใส่เบอร์มือถือ 10 หลัก</label>
      <input name="phone" placeholder="062xxxxxxx" required maxlength="10">

      <label>ใส่จำนวน (นาที)</label>
      <input name="amount" placeholder="จำนวนที่ต้องการยิง" required>

      <button type="submit">เริ่มการยิงเบอร์</button>
    </form>

    {% if message %}
      <div class="msg {{ 'ok' if ok else 'err' }}">{{ message }}</div>
    {% endif %}

    <div class="note">หมายเหตุ: จำนวนต้องอยู่ในช่วง 1-{{X}}</div>
  </div>
</body>
</html>
"""

STATUS_HTML = """
<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>สถานะการยิงเบอร์</title>
  <style>
    body{font-family:sans-serif;background:#0b0f19;color:#fff;display:flex;justify-content:center;padding:30px}
    .card{width:100%;max-width:620px;background:#121a2b;border-radius:16px;padding:22px;box-shadow:0 10px 30px rgba(0,0,0,.4)}
    h1{margin:0 0 14px;font-size:22px}
    .row{margin:10px 0;padding:12px;border-radius:12px;background:#0b1220;border:1px solid #2a3552}
    .green{color:#2bd576;font-weight:700}
    .red{color:#ff4d4d;font-weight:700}
    .muted{color:#94a3b8}
    a{color:#60a5fa}
    .bar{height:10px;background:#0b1220;border:1px solid #2a3552;border-radius:999px;overflow:hidden}
    .bar > div{height:100%;width:0%}
  </style>
</head>
<body>
  <div class="card">
    <h1>สถานะการยิงเบอร์</h1>

    {% if not job %}
      <div class="row red">ไม่พบงานนี้</div>
      <a href="/">กลับหน้าหลัก</a>
    {% else %}
      <div class="row">📵 เบอร์: <b>{{job.phone}}</b></div>
      <div class="row">⏱️ เวลา: <b>{{job.amount}}</b> นาที</div>

      <div class="row">
        สถานะ:
        {% if job.status == 'running' %}
          <span class="green">🟢 กำลังยิง</span>
        {% elif job.status == 'done' %}
          <span class="red">🔴 หมดเวลาแล้ว</span>
        {% else %}
          <span class="red">❌ Error</span>
          <div class="muted">{{job.error}}</div>
        {% endif %}
      </div>

      <div class="row">
        เหลือเวลา: <b id="remain">...</b>
        <div style="margin-top:10px" class="bar"><div id="bar"></div></div>
      </div>

      <div class="muted">หน้านี้จะอัปเดตอัตโนมัติ</div>
      <div style="margin-top:10px"><a href="/">เริ่มงานใหม่</a></div>
    {% endif %}
  </div>

<script>
async function refresh() {
  const res = await fetch("{{ url_for('api_status', job_id=job_id) }}");
  const data = await res.json();

  if (!data.ok) return;

  const remainEl = document.getElementById("remain");
  const barEl = document.getElementById("bar");

  let remain = data.remain_seconds;
  if (remain < 0) remain = 0;

  const m = Math.floor(remain / 60);
  const s = Math.floor(remain % 60);
  remainEl.textContent = `${m} นาที ${s} วินาที`;

  barEl.style.width = `${data.progress_percent}%`;

  // รีเฟรชทุก 1 วิ
  setTimeout(refresh, 1000);

  // ถ้าจบแล้ว reload เพื่อโชว์สถานะล่าสุด
  if (data.status !== "running") {
    setTimeout(()=>location.reload(), 1500);
  }
}
refresh();
</script>
</body>
</html>
"""

def run_job(job_id: str):
    job = JOBS[job_id]
    phone = job["phone"]
    amount = str(job["amount"])

    try:
        subprocess.Popen(["python", "sms.py", phone, amount])
        # amount ในไฟล์เดิมเป็นนาที แต่ในโค้ดเดิมพี่ sleep(amount) (วินาที)
        # เว็บนี้ทำให้ "ถูกต้อง" = นาทีจริง
        time.sleep(job["amount"] * 60)
        job["status"] = "done"
    except Exception as e:
        job["status"] = "error"
        job["error"] = str(e)

@app.get("/")
def index():
    return render_template_string(INDEX_HTML, message=None, ok=True, X=X)

@app.post("/send")
def send():
    phone = request.form.get("phone", "").strip()
    amount = request.form.get("amount", "").strip()

    # ตรวจสอบ phone
    if not (phone.isdigit() and len(phone) == 10):
        return render_template_string(INDEX_HTML, message="กรุณาใส่เบอร์มือถือให้ครบ 10 หลัก", ok=False, X=X)

    # ตรวจสอบ amount
    if not amount.isdigit() or not (1 <= int(amount) <= X):
        return render_template_string(INDEX_HTML, message=f"จำนวนที่ต้องการยิงต้องอยู่ในช่วง 1-{X}", ok=False, X=X)

    minutes = int(amount)

    job_id = str(uuid.uuid4())[:8]
    now = time.time()

    JOBS[job_id] = {
        "phone": phone,
        "amount": minutes,
        "start_time": now,
        "end_time": now + (minutes * 60),
        "status": "running",
        "error": ""
    }

    t = threading.Thread(target=run_job, args=(job_id,), daemon=True)
    t.start()

    return redirect(url_for("status_page", job_id=job_id))

@app.get("/status/<job_id>")
def status_page(job_id):
    job = JOBS.get(job_id)
    return render_template_string(STATUS_HTML, job=job, job_id=job_id)

@app.get("/api/status/<job_id>")
def api_status(job_id):
    job = JOBS.get(job_id)
    if not job:
        return {"ok": False, "error": "not_found"}

    now = time.time()
    total = job["end_time"] - job["start_time"]
    remain = job["end_time"] - now
    done = total - remain

    if total <= 0:
        progress = 100
    else:
        progress = int(max(0, min(100, (done / total) * 100)))

    return {
        "ok": True,
        "status": job["status"],
        "phone": job["phone"],
        "amount": job["amount"],
        "remain_seconds": int(remain),
        "progress_percent": progress
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)



