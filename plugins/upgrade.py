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
	💵Price Rs 50 per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 20 GB💫
	💵Price Rs 80 per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 50 GB💫
	💵Price Rs 140 per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 70 GB💫
	💵Price Rs 180 per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 100 GB💫
	💵Price Rs 220 per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	
	⛩️TEAM PLANS - FOR 1 TO 4 MEMBERS⛩️
	
	✨ Platinum Tier ✨ 
	💫Daily 50 GB For Each Person in Team💫
	💵Price Rs 200 per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit UNLIMITED💫
	💵Price Rs 400 per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	⚠️*********NOTE**********⚠️
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96
	
	⚠️*********NOTE**********⚠️"""
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
	💵Price Rs 50 per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 20 GB💫
	💵Price Rs 80 per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 50 GB💫
	💵Price Rs 140 per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 70 GB💫
	💵Price Rs 180 per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 100 GB💫
	💵Price Rs 220 per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	
	⛩️TEAM PLANS - FOR 1 TO 4 MEMBERS⛩️
	
	✨ Platinum Tier ✨ 
	💫Daily 50 GB For Each Person in Team💫
	💵Price Rs 200 per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit UNLIMITED💫
	💵Price Rs 400 per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	⚠️*********NOTE**********⚠️
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96
	
	⚠️*********NOTE**********⚠️"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
