import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7993052115:AAGM58l-JJfaAU7nD8ho80_PKuU8haLGFIA"

# কাস্টমার ডাটাবেজ (মেমোরি)
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
        [InlineKeyboardButton("🎧 Support Center", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    msg = f"⚡ **WELCOME TO OLD X HACKER SHOP** ⚡\n\nনিচের বাটনগুলো ব্যবহার করে সেবা নিন:"
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

    # মূল মেনু
    if data == "main_menu":
        await start(update, context)

    # প্রফাইল
    elif data == "profile":
        text = (
            f"👤 **YOUR PROFILE**\n"
            f"═══════════════════════\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"👤 **Name:** {user_data['name']}\n\n"
            f"💰 **Balance Details**\n"
            f"💵 **Current:** ৳{user_data['balance']}\n\n"
            f"📊 **Statistics**\n"
            f"📦 **Total Orders:** {len(user_data['orders'])}\n"
            f"💸 **Total Spent:** ৳{user_data['spent']}\n"
            f"💳 **Total Deposited:** ৳{user_data['deposited']}\n"
            f"🎁 **Referral Earned:** ৳{user_data['referral_earned']}\n\n"
            f"🔗 **Your Referral Link:**\n"
            f"https://t.me/MurubbixshoppBot?start=ref_{user_id}\n\n"
            f"📊 Share and earn 10% commission on purchases!"
        )
        keyboard = [
            [InlineKeyboardButton("📦 My Orders", callback_data="my_orders"), InlineKeyboardButton("💳 Add Balance", callback_data="add_balance")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # শপ ক্যাটাগরি
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

    # BALA MOD
    elif data == "prod_bala":
        text = (
            "🎮 **BALA MOD**\n\n"
            "📊 **STOCK & PRICING:**\n"
            "═══════════════════════\n"
            "**1 Hour** | Stock: ✅ In Stock | Price: ৳25\n"
            "**3 Hours** | Stock: ✅ In Stock | Price: ৳70\n"
            "**6 Hours** | Stock: ✅ In Stock | Price: ৳140\n"
            "**12 Hours** | Stock: ✅ In Stock | Price: ৳270\n"
            "**24 Hours** | Stock: ✅ In Stock | Price: ৳500\n"
            "**2 Days** | Stock: ✅ In Stock | Price: ৳900\n"
            "**3 Days** | Stock: ✅ In Stock | Price: ৳1,300\n"
            "**7 Days** | Stock: ✅ In Stock | Price: ৳3,000\n\n"
            "👉 **SELECT YOUR PLAN:**"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 1 Hour - ৳25", callback_data="pay_bala_1h")],
            [InlineKeyboardButton("🛒 Buy 3 Hours - ৳70", callback_data="pay_bala_3h")],
            [InlineKeyboardButton("🛒 Buy 6 Hours - ৳140", callback_data="pay_bala_6h")],
            [InlineKeyboardButton("🛒 Buy 12 Hours - ৳270", callback_data="pay_bala_12h")],
            [InlineKeyboardButton("🛒 Buy 24 Hours - ৳500", callback_data="pay_bala_24h")],
            [InlineKeyboardButton("🛒 Buy 2 Days - ৳900", callback_data="pay_bala_2d")],
            [InlineKeyboardButton("🛒 Buy 3 Days - ৳1,300", callback_data="pay_bala_3d")],
            [InlineKeyboardButton("🛒 Buy 7 Days - ৳3,000", callback_data="pay_bala_7d")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # DRIP CLIENT PROXY
    elif data == "prod_drip":
        text = (
            "💻 **DRIP CLIENT PROXY**\n\n"
            "📊 **STOCK & PRICING:**\n"
            "═══════════════════════\n"
            "**1 Day** | Stock: ✅ In Stock | Price: ৳100\n"
            "**3 Days** | Stock: ✅ In Stock | Price: ৳200\n"
            "**7 Days** | Stock: ✅ In Stock | Price: ৳400\n"
            "**30 Days** | Stock: ✅ In Stock | Price: ৳800\n\n"
            "👉 **SELECT YOUR PLAN:**"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 1 Day - ৳100", callback_data="pay_drip_1d")],
            [InlineKeyboardButton("🛒 Buy 3 Days - ৳200", callback_data="pay_drip_3d")],
            [InlineKeyboardButton("🛒 Buy 7 Days - ৳400", callback_data="pay_drip_7d")],
            [InlineKeyboardButton("🛒 Buy 30 Days - ৳800", callback_data="pay_drip_30d")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # BRMOD PC
    elif data == "prod_brmod":
        text = (
            "🖥️ **BRMOD PC**\n\n"
            "📊 **STOCK & PRICING:**\n"
            "═══════════════════════\n"
            "**1 Day** | Stock: ✅ In Stock | Price: ৳100\n"
            "**10 Days** | Stock: ✅ In Stock | Price: ৳450\n"
            "**30 Days** | Stock: ✅ In Stock | Price: ৳750\n\n"
            "👉 **SELECT YOUR PLAN:**"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 1 Day - ৳100", callback_data="pay_brmod_1d")],
            [InlineKeyboardButton("🛒 Buy 10 Days - ৳450", callback_data="pay_brmod_10d")],
            [InlineKeyboardButton("🛒 Buy 30 Days - ৳750", callback_data="pay_brmod_30d")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # XREG ANDROID+IOS
    elif data == "prod_xreg":
        text = (
            "📱 **XREG ANDROID+IOS**\n\n"
            "📊 **STOCK & PRICING:**\n"
            "═══════════════════════\n"
            "**1 Hour** | Stock: ✅ In Stock | Price: ৳20\n"
            "**3 Hours** | Stock: ✅ In Stock | Price: ৳50\n"
            "**6 Hours** | Stock: ✅ In Stock | Price: ৳80\n"
            "**12 Hours** | Stock: ✅ In Stock | Price: ৳110\n"
            "**1 Day** | Stock: ✅ In Stock | Price: ৳160\n"
            "**3 Days** | Stock: ✅ In Stock | Price: ৳250\n"
            "**7 Days** | Stock: ✅ In Stock | Price: ৳400\n"
            "**30 Days** | Stock: ✅ In Stock | Price: ৳1,000\n\n"
            "👉 **SELECT YOUR PLAN:**"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 1 Hour - ৳20", callback_data="pay_xreg_1h")],
            [InlineKeyboardButton("🛒 Buy 3 Hours - ৳50", callback_data="pay_xreg_3h")],
            [InlineKeyboardButton("🛒 Buy 6 Hours - ৳80", callback_data="pay_xreg_6h")],
            [InlineKeyboardButton("🛒 Buy 12 Hours - ৳110", callback_data="pay_xreg_12h")],
            [InlineKeyboardButton("🛒 Buy 1 Day - ৳160", callback_data="pay_xreg_1d")],
            [InlineKeyboardButton("🛒 Buy 3 Days - ৳250", callback_data="pay_xreg_3d")],
            [InlineKeyboardButton("🛒 Buy 7 Days - ৳400", callback_data="pay_xreg_7d")],
            [InlineKeyboardButton("🛒 Buy 30 Days - ৳1,000", callback_data="pay_xreg_30d")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # FREE FIRE LIKES
    elif data == "prod_ff_likes":
        text = (
            "👍 **FREE FIRE LIKES**\n\n"
            "আপনার Free Fire অ্যাকাউন্টে সরাসরি real likes পাঠিয়ে দেওয়া হবে – নিরাপদ ও দ্রুত।\n\n"
            "🎁 **প্যাকেজ বেছে নিন:**\n"
            "🥊 100 Likes – ৳10\n"
            "🔥 200 Likes – ৳20\n\n"
            "👇 **নিচের বাটনে ট্যাপ করে শুরু করুন**"
        )
        keyboard = [
            [InlineKeyboardButton("🥊 100 Likes - ৳10", callback_data="pay_ff_100")],
            [InlineKeyboardButton("🔥 200 Likes - ৳20", callback_data="pay_ff_200")],
            [InlineKeyboardButton("📜 আমার History", callback_data="my_orders")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # পেমেন্ট মেথড
    elif data.startswith("pay_"):
        text = (
            "💳 **SELECT PAYMENT METHOD**\n"
            "═══════════════════════\n\n"
            "💵 **Your Balance:** ৳" + str(user_data["balance"]) + "\n\n"
            "👉 **CHOOSE PAYMENT:**"
        )
        keyboard = [
            [InlineKeyboardButton("💳 Pay via bKash / Nagad / Bank", callback_data="add_balance")],
            [InlineKeyboardButton("💰 Pay with Balance", callback_data="add_balance")],
            [InlineKeyboardButton("🔙 Back", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # মাই অর্ডারস
    elif data == "my_orders":
        if not user_data["orders"]:
            text = "📦 **MY ORDERS**\n\nএখনো কোনো order নেই! Shop থেকে কেনাকাটা শুরু করুন!"
        else:
            text = "📦 **MY ORDERS**\n\n" + "\n".join(user_data["orders"])
        keyboard = [
            [InlineKeyboardButton("🛍️ Continue Shopping", callback_data="shop")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # অ্যাড ব্যালেন্স ও পেমেন্ট নম্বর
    elif data == "add_balance":
        text = (
            "💳 **PAYMENT DETAILS / ADD BALANCE**\n"
            "═══════════════════════\n\n"
            "নিচের যেকোনো মাধ্যমে টাকা পাঠান:\n\n"
            "📱 **bKash (Personal):** `01998307838`\n"
            "📱 **Nagad (Personal):** `01633900777`\n"
            "🏦 **Bank Account:** `20500030300948700`\n\n"
            "📌 **টাকা পাঠানোর পর:**\n"
            "Transaction ID (TrxID) এবং আপনার ইমেইল/আইডি আমাদের সাপোর্ট অ্যাকাউন্টে পাঠান।"
        )
        keyboard = [
            [InlineKeyboardButton("🎧 Send TrxID to Support", url="https://t.me/OLDXHACKER0")],
            [InlineKeyboardButton("📢 Join Group", url="https://t.me/+yMXOZHuy5Wk5ZWI1")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # সাপোর্ট সেন্টার
    elif data == "support":
        text = (
            "🎧 **SUPPORT CENTER**\n"
            "═══════════════════════\n\n"
            "💬 কোনো সমস্যা হলে বা ব্যালেন্স যুক্ত করতে নিচের বাটনে ক্লিক করে সরাসরি যোগাযোগ করুন।"
        )
        keyboard = [
            [InlineKeyboardButton("💬 Contact Admin (@OLDXHACKER0)", url="https://t.me/OLDXHACKER0")],
            [InlineKeyboardButton("📢 Telegram Group", url="https://t.me/+yMXOZHuy5Wk5ZWI1")],
            [InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
