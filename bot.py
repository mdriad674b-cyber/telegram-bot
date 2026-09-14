import http.server
import socketserver
import threading
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# --- Render Port Binding (Dummy HTTP Server) ---
def run_dummy_server():
    PORT = 10000
    Handler = http.server.SimpleHTTPRequestHandler
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except Exception:
        pass

threading.Thread(target=run_dummy_server, daemon=True).start()

# --- Configuration & Links ---
BOT_TOKEN = "7993052115:AAGM58l-JJfaAU7nD8ho80_PKuU8haLGFIA"
SUPPORT_LINK = "https://t.me/riad3657"
GROUP_LINK = "https://t.me/OldXShopBot"

# --- UI Keyboards ---
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("🛍 Shop Now", callback_data="shop_now")],
        [InlineKeyboardButton("👤 Profile", callback_data="profile"), InlineKeyboardButton("🎯 FF Likes", callback_data="ff_likes")],
        [InlineKeyboardButton("💳 Add Balance", callback_data="add_balance"), InlineKeyboardButton("🎁 Referral", callback_data="referral")],
        [InlineKeyboardButton("🎰 Lucky Spin", callback_data="lucky_spin"), InlineKeyboardButton("📁 Files", callback_data="files")],
        [InlineKeyboardButton("📺 Tutorials", callback_data="tutorials"), InlineKeyboardButton("☎️ Support", callback_data="support")]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_button = KeyboardButton(text="📱 Share Phone Number", request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True, one_time_keyboard=True)
    
    msg = (
        "📱 **Phone Number Verify করুন**\n\n"
        "Bot ব্যবহার করার আগে আপনার phone number verify করা প্রয়োজন।\n\n"
        "নিচের বাটনে ক্লিক করে আপনার number শেয়ার করুন 👇"
    )
    await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=reply_markup)

async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        "✅ **Phone number verify হয়ে গেছে! ধন্যবাদ।**\n\n"
        "═════════════════════\n"
        "🎮 **OLD X SHOP** 🎮\n"
        "═════════════════════\n\n"
        f"Hey {user.first_name} 👋, glad to have you here.\n\n"
        "**যা যা পাচ্ছেন এখানে:**\n"
        " 🔑 Premium Game Keys\n"
        " ⚡️ Instant 24/7 Delivery\n"
        " 🔒 100% Secure Payment\n"
        " 💸 Best Price Guarantee\n"
        " 🎁 Referral Rewards\n"
        " 🏆 Real Human Support\n\n"
        "═════════════════════\n"
        "👇 **নিচ থেকে শুরু করুন**"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown", reply_markup=get_main_menu())

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    data = query.data

    if data == "shop_now" or data == "back_to_shop":
        text = (
            "🛒 **BRMOD PC**\n\n"
            "📊 **STOCK & PRICING:**\n"
            "═════════════════════\n\n"
            "**1 Day**\n"
            "📦 Stock: ✅ In Stock\n"
            "💰 Price: ৳100\n\n"
            "**10 Days**\n"
            "📦 Stock: ✅ In Stock\n"
            "💰 Price: ৳450\n\n"
            "**30 Days**\n"
            "📦 Stock: ✅ In Stock\n"
            "💰 Price: ৳750\n\n"
            "🎯 **SELECT YOUR PLAN:**"
        )
        keyboard = [
            [InlineKeyboardButton("🛒 Buy 1 Day - ৳100", callback_data="buy_1")],
            [InlineKeyboardButton("🛒 Buy 10 Days - ৳450", callback_data="buy_10")],
            [InlineKeyboardButton("🛒 Buy 30 Days - ৳750", callback_data="buy_30")],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_to_main")]
        ]
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "profile":
        text = (
            "👤 **YOUR PROFILE**\n"
            "═════════════════════\n\n"
            "🆔 **Account Information**\n\n"
            f"🆔 User ID: `{user.id}`\n"
            f"👤 Name: {user.first_name}\n\n"
            "💰 **Balance Details**\n\n"
            "💵 Current: ৳0\n\n"
            "📊 **Statistics**\n\n"
            "📦 Total Orders: 0\n"
            "💸 Total Spent: ৳0\n"
            "🏦 Total Deposited: ৳0\n"
            "🎁 Referral Earned: ৳0\n\n"
            "🔗 **Your Referral Link**\n"
            "═════════════════════\n\n"
            f"https://t.me/OldXShopBot?start=ref_{user.id}\n\n"
            "📊 Share and earn 10% commission on purchases!"
        )
        keyboard = [
            [InlineKeyboardButton("📦 My Orders", callback_data="my_orders")],
            [InlineKeyboardButton("💳 Add Balance", callback_data="add_balance")],
            [InlineKeyboardButton("📜 Transaction", callback_data="transaction")],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_to_main")]
        ]
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "support":
        text = (
            "💳 **SUPPORT CENTER**\n"
            "═════════════════════\n\n"
            "💬 কোনো সমস্যা হলে নিচের বাটনে ক্লিক করে আমাদের সাথে সরাসরি যোগাযোগ করুন।"
        )
        keyboard = [
            [InlineKeyboardButton("💬 Support এ যোগাযোগ করুন", url=SUPPORT_LINK)],
            [InlineKeyboardButton("📢 Join Group", url=GROUP_LINK)],
            [InlineKeyboardButton("⬅️ Back to Shop", callback_data="back_to_shop")]
        ]
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "back_to_main":
        welcome_text = (
            "═════════════════════\n"
            "🎮 **OLD X SHOP** 🎮\n"
            "═════════════════════\n\n"
            f"Hey {user.first_name} 👋, glad to have you here.\n\n"
            "**যা যা পাচ্ছেন এখানে:**\n"
            " 🔑 Premium Game Keys\n"
            " ⚡️ Instant 24/7 Delivery\n"
            " 🔒 100% Secure Payment\n"
            " 💸 Best Price Guarantee\n"
            " 🎁 Referral Rewards\n"
            " 🏆 Real Human Support\n\n"
            "═════════════════════\n"
            "👇 **নিচ থেকে শুরু করুন**"
        )
        await query.edit_message_text(welcome_text, parse_mode="Markdown", reply_markup=get_main_menu())

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shop", start))
    app.add_handler(MessageHandler(filters.CONTACT, contact_handler))
    app.add_handler(CallbackQueryHandler(button_click))
    
    app.run_polling()

if __name__ == "__main__":
    main()
