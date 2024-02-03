import requests
import re, os
import json
import time

ses = requests.Session()
ua_ig = "Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)"

def clear():
  os.system("clear")
  
def bot(header, token):
  with ses as req:
    try:
      headers = {
        "Host": "i.instagram.com",
        "content-length": "0",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        "x-ig-app-id": "1217981644879628",
        "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
        "sec-ch-ua-mobile": "?1",
        "x-instagram-ajax": "1006447742",
        "viewport-width": "360",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "user-agent": ua_ig,
        "x-asbd-id": "198387",
        "save-data": "on",
        "x-csrftoken": token,
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://www.instagram.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.instagram.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"
      }
    except requests.exceptions.ConnectionError:
      print("anda tidak memiliki koneksi internet")

def cek_cookie():
  clear()
  cook = input("Masukkan Cookie: ")
  try:
      with ses as req:
          headers = {"user-agent": ua_ig}
          cookies = {"cookie": cook}
          link = req.get(
              "https://i.instagram.com/api/v1/users/{}/info/".format(
                  re.search('ds_user_id=(.*?);', str(cook)).group(1)
              ),
              headers=headers,
              cookies=cookies,
          ).json()["user"]["full_name"]
          print(f"anda berhasil login {link}")
          bot(cook, re.search('csrftoken=(.*?);', str(cook)).group(1))
  except (AttributeError, KeyError):
      print("cookie anda telah kadarluarsa")
     
cek_cookie()