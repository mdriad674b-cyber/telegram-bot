import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ---------------------------------------------------------
# 1. FLASK WEB SERVER (Render & UptimeRobot Support)
# ---------------------------------------------------------
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "OLD X HACKER SHOP BOT IS RUNNING LIVE 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)

# ---------------------------------------------------------
# 2. TELEGRAM BOT CONFIGURATION
# ---------------------------------------------------------
TOKEN = "7993052115:AAGM58l-JJfaAU7nD8ho80_PKuU8haLGFIA"

users = {}

def get_user(user_id, name):
    if user_id not in users:
        users[user_id] = {
            "name": name,
            "balance": 0,
            "orders": [],
            "spent": 0,
            "deposited": 0,
            "referral_earned": 0
        }
    return users[user_id]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    get_user(user.id, user.first_name)
    
    keyboard = [
        [InlineKeyboardButton("🛒 Shop", callback_data="shop"), InlineKeyboardButton("👤 Profile", callback_data="profile")],
        [InlineKeyboardButton("📦 My Orders", callback_data="my_orders"), InlineKeyboardButton("💳 Add Balance", callback_data="add_balance")],
        [InlineKeyboardButton("📢 Join Group / Community", url="https://t.me/+yMXOZHuy5Wk5ZWI1")],
        [InlineKeyboardButton("🎧 Support Center", url="https://t.me/OLDXHACKER0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    msg = f"⚡ **WELCOME TO OLD X HACKER SHOP** ⚡\n\nনিচের বাটনগুলো ব্যবহার করে আপনার সার্ভিস নির্বাচন করুন:"
    if update.callback_query:
        await update.callback_query.message.edit_text(msg, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.message.reply_text(msg, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id
    user_data = get_user(user_id, query.from_user.first_name)

    if data == "main_menu":
        await start(update, context)

    elif data == "profile":
        text = (
            f"👤 **YOUR PROFILE**\n"
            f"═══════════════════════\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"👤 **Name:** {user_data['name']}\n\n"
            f"💰 **Balance:** ৳{user_data['balance']}\n"
            f"📦 **Total Orders:** {len(user_data['orders'])}\n"
            f"💸 **Total Spent:** ৳{user_data['spent']}\n"
            f"💳 **Total Deposited:** ৳{user_data['deposited']}\n\n"
            f"🔗 **Your Referral Link:**\n"
            f"https://t.me/MurubbixshoppBot?start=ref_{user_id}"
        )
        keyboard = [
            [InlineKeyboardButton("💳 Add Balance", callback_data="add_balance")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "shop":
        text = "🛒 **SELECT PRODUCT CATEGORY:**"
        keyboard = [
            [InlineKeyboardButton("🎮 BALA MOD", callback_data="prod_bala")],
            [InlineKeyboardButton("💻 DRIP CLIENT PROXY", callback_data="prod_drip")],
            [InlineKeyboardButton("🖥️ BRMOD PC", callback_data="prod_brmod")],
            [InlineKeyboardButton("📱 XREG ANDROID+IOS", callback_data="prod_xreg")],
            [InlineKeyboardButton("👍 FREE FIRE LIKES", callback_data="prod_ff_likes")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "prod_bala":
        text = (
            "🎮 **BALA MOD**\n\n"
            "**1 Hour** - ৳25 | **3 Hours** - ৳70\n"
            "**6 Hours** - ৳140 | **12 Hours** - ৳270\n"
            "**24 Hours** - ৳500 | **7 Days** - ৳3,000\n"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 1 Hour (৳25)", callback_data="add_balance")],
            [InlineKeyboardButton("🛒 Buy 24 Hours (৳500)", callback_data="add_balance")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "prod_ff_likes":
        text = (
            "👍 **FREE FIRE LIKES (REAL PANEL)**\n\n"
            "🥊 **100 Likes** – ৳10\n"
            "🔥 **200 Likes** – ৳20\n"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 100 Likes - ৳10", callback_data="add_balance")],
            [InlineKeyboardButton("🛒 Buy 200 Likes - ৳20", callback_data="add_balance")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "add_balance":
        text = (
            "💳 **OLD X HACKER SHOP PAYMENT**\n"
            "═══════════════════════\n\n"
            "নিচের যেকোনো একাউন্টে টাকা পাঠিয়ে Admin-কে TrxID পাঠান:\n\n"
            "📱 **bKash (Personal):** `01998307838`\n"
            "📱 **Nagad (Personal):** `01633900777`\n"
            "🏦 **Bank Account:** `20500030300948700`\n\n"
            "📌 **টাকা পাঠানোর পর:**\n"
            "নিচের 'Send TrxID' বাটনে ক্লিক করে এডমিনকে স্ক্রিনশট ও TrxID দিন।"
        )
        keyboard = [
            [InlineKeyboardButton("📩 Send TrxID to Admin", url="https://t.me/OLDXHACKER0")],
            [InlineKeyboardButton("📢 Join Telegram Group", url="https://t.me/+yMXOZHuy5Wk5ZWI1")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "my_orders":
        text = "📦 **MY ORDERS**\n\nআপনার কোনো সক্রিয় অর্ডার নেই।"
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

def main():
    # Flask থ্রেড রান
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()

    # Telegram Bot রান
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
