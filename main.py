from os import system 
import os,sys,time,requests
import random, telebot, os
from time import sleep
from telebot import types
import requests
from os import system 
import os,sys,time,requests
try:
	Info = open("info.txt").read()
except:
	Info = "Ali"	
if ":" not in Info:
	token ="6002155062:AAHnR6j9qmRJ1mReNmkWSJm-wcngqQTvUvc";reqtoken = requests.get(f"https://api.telegram.org/bot{token}/getme").json();req = reqtoken["ok"]
	if req == True:
		id ="1308075085"
		o = open("info.txt",'a').write(str(token)+'\n'+str(id))
		print("Done .")
	else:
		print("Erorr ToKeN .")
else:
	print("Ok .")
info = open("info.txt",'r').read();token = info.split('\n')[0];own_id = info.split('\n')[1]
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    global id, name
    id = message.from_user.id
    name = message.from_user.first_name
    print(name+" - "+str(id))
    mar= types.ReplyKeyboardMarkup(resize_keyboard=True)
    try:
    	y = open("ID.txt").read()
    	user = y.replace("@", "")
    except:
    	user = "None"
    try:
    	y = (open("sleep.txt").read())
    	sleep = y.replace(" ", "")
    except:
    	sleep = "0.5"
    A = types.KeyboardButton(f"@{user}")
    B = types.KeyboardButton("〔 Add User 〕")
    D = types.KeyboardButton(f" Sleep {sleep} ")
    E = types.KeyboardButton("〔 Add Sleep 〕")
    G = types.KeyboardButton("〔 Start 〕")
    H = types.KeyboardButton("〔 Stop 〕")
    R = types.KeyboardButton("〔 Sections Number 〕")
    mar.add(A)
    mar.add(G,H)
    mar.add(B)
    mar.add(D,E)
    mar.add(R)
    ph = "https://telegra.ph/file/8583e7d11d10a0d4c758c.mp4"
    if str(id) == own_id:
    	bot.send_video(message.chat.id,ph,caption=f"""*- الإمام علي (عليه السلام): إن رسول الله (صلى الله عليه وآله) أدبه الله عز وجل، وهو أدبني، وأنا أؤدب المؤمنين، وأورث الأدب المكرمين  , {message.chat.first_name} .*""",parse_mode="markdown",reply_markup=mar)
@bot.message_handler(func=lambda m:True)
def text(message):
 	acc = message.text
 	id = message.from_user.id
 	if str(id) == own_id:
 		h = "https://telegra.ph/file/0f0fbaa8d8e696e4288b6.mp4"
 		if acc == "〔 Add User 〕":
 				bot.send_video(message.chat.id,h, caption="Pin User /ID @aaaaa")
 		if acc == "〔 Add Sleep 〕":
 			bot.send_message(message.chat.id, text=" 《 Send /sleep 0 or anything you needed 》 ")
 		if "/ID" in acc and "@" in acc:
 			try:
 				print(os.remove("ID.txt"))
 				bot.send_message(message.chat.id, text="Done Delete User .")
 			except:
 				bot.send_message(message.chat.id, text="Dont Here User !")
 			a = acc.replace("/ID", "")
 			o = a.replace(" ", "")
 			try:
 				with open('ID.txt', 'a') as the_combo:
 					the_combo.write(str(o))
 				bot.send_message(message.chat.id, text="《 Done added This User 》")
 			except:
 				bot.send_message(message.chat.id, text="This Error : Try Again")
 		if "/sleep" in acc:
 			try:
 				os.remove("sleep.txt")
 			except:
 				pass
 			a = acc.replace("/sleep", "")
 			o = a.replace(" ", "")
 			try:
 				with open('sleep.txt', 'a') as the_combo:
 					the_combo.write(str(o))
 				bot.send_message(message.chat.id, text="《 Done Add This Sleep 》")
 			except:
 				bot.send_message(message.chat.id, text="This Error : Try Again")
 		if acc == "〔 Start 〕":
 			try:
 				bot.send_message(message.chat.id, text="Done .")
 				system("screen -S Bot -X kill")
 				system("screen -S Bot python3 bot.py")
 			except:
 				pass
 		if acc == "〔 Stop 〕":
 			try:
 				system("screen -S Bot -X kill")
 			except:
 				pass
 			bot.send_message(message.chat.id, text="Done .")
 		if acc == "/RemoveAll":
 			try:
 				os.remove("Number.txt")
 				bot.send_message(message.chat.id, text="- Done ")
 			except:
 				bot.send_message(message.chat.id, text="Dont There Number")
 		if acc == "〔 Sections Number 〕":
        	 bot.send_message(message.chat.id, text="1 - /RemoveAll To Deleted All Number -- 2 - /Count_Number To Know how many Number in bot -- 3 - /add with session for login number session pyrogram only .")
 		if acc == "/Count_Number":
 			try:
 				document = open('Number.txt', 'rb')
 				w = len(open("Number.txt").readlines())
 				bot.send_document(message.chat.id,document,caption=f"- The Number  : {w}")
 			except:
 				bot.send_message(message.chat.id, text="Dont There Number")
 	if "/add" in acc:
 			ks = acc.replace("/add", "")
 			k = ks.replace(" ", "")
 			try:
 				with open('Number.txt', 'a') as the_combo:
 					the_combo.write(str(k)+'\n')
 				bot.send_message(message.chat.id, text="Done Login")
 			except:
 				bot.send_message(message.chat.id, text="- Error , try Again.")
bot.polling(none_stop=True)