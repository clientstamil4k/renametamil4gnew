"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	⛩️INDIVIDUAL PLAN - FOR 1 MEMBER⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 10 or 0.5$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 25 GB💫
	💵Price Rs 20 or 1$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 30 or 1.5$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 70 GB💫
	💵Price Rs 50 or 2$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 150 GB💫
	💵Price Rs 100 or 3$ per Month💵
	
	Pay Using Upi I'd ```karna862001-1@okicici```
	
	
	
	⛩️TEAM PLANS - FOR 1 TO 4 MEMBERS⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 20 or 0.7$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 25 GB💫
	💵Price Rs 40 or 1.2$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 60 or 2$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 70 GB💫
	💵Price Rs 100 or 3$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 150 GB💫
	💵Price Rs 200 or 5$ per Month💵
	
	Pay Using Upi I'd ```karna862001-1@okicici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	
	⛩️INDIVIDUAL PLAN - FOR 1 MEMBER⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 10 or 0.5$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 25 GB💫
	💵Price Rs 20 or 1$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 30 or 1.5$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 70 GB💫
	💵Price Rs 50 or 2$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 150 GB💫
	💵Price Rs 100 or 3$ per Month💵
	
	Pay Using Upi I'd ```karna862001-1@okicici```
	
	
	
	⛩️TEAM PLANS - FOR 1 TO 4 MEMBERS⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 20 or 0.7$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 25 GB💫
	💵Price Rs 40 or 1.2$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 60 or 2$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 70 GB💫
	💵Price Rs 100 or 3$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 150 GB💫
	💵Price Rs 200 or 5$ per Month💵
	
	Pay Using Upi I'd ```karna862001-1@okicici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
