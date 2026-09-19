import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Flask Web Server (Render Live রাখার জন্য)
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

logging.basicConfig(level=logging.INFO)

# Main Menu Keyboards
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop Now", callback_data='shop'), InlineKeyboardButton("💎 FF Likes", callback_data='ff_likes')],
        [InlineKeyboardButton("👤 Profile", callback_data='profile'), InlineKeyboardButton("👥 Referral", callback_data='referral')],
        [InlineKeyboardButton("💳 Add Balance", callback_data='add_balance'), InlineKeyboardButton("🎰 Lucky Spin", callback_data='lucky_spin')],
        [InlineKeyboardButton("📁 Files", callback_data='files'), InlineKeyboardButton("📚 Tutorials", callback_data='tutorials')],
        [InlineKeyboardButton("💬 Support", callback_data='support')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "<b>WELCOME TO OLD X SHOP!</b>\n\nনিচের বাটনগুলো ব্যবহার করে আপনার প্রয়োজনীয় অপশন সিলেক্ট করুন:"
    if update.message:
        await update.message.reply_text(welcome_text, parse_mode='HTML', reply_markup=main_menu_keyboard())
    elif update.callback_query:
        await update.callback_query.message.edit_text(welcome_text, parse_mode='HTML', reply_markup=main_menu_keyboard())

# Button Handlers
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'main_menu':
        await start(update, context)

    elif query.data == 'add_balance':
        payment_text = (
            "<b>💳 OLD X SHOP PAYMENT METHOD</b>\n\n"
            "নিচের যেকোনো একাউন্টে টাকা পাঠিয়ে Admin-কে TrxID পাঠান:\n\n"
            "📱 <b>bKash (Personal):</b> <code>01800000000</code>\n"
            "📱 <b>Nagad (Personal):</b> <code>01700000000</code>\n"
            "🏦 <b>Bank Account:</b> <code>1234567890</code>\n\n"
            "📌 <b>টাকা পাঠানোর পর:</b>\n"
            "নিচের <i>Send TrxID to Admin</i> বাটনে ক্লিক করে এডমিনকে স্ক্রিনশট ও TrxID দিন।"
        )
        keyboard = [
            [InlineKeyboardButton("📩 Send TrxID to Admin", url="https://t.me/your_admin_username")],
            [InlineKeyboardButton("📢 Join Telegram Group", url="https://t.me/your_group_link")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text(payment_text, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'profile':
        user = query.from_user
        profile_text = f"<b>👤 USER PROFILE</b>\n\n<b>Name:</b> {user.first_name}\n<b>User ID:</b> <code>{user.id}</code>\n<b>Balance:</b> ৳0.00"
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='main_menu')]]
        await query.message.edit_text(profile_text, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        text = f"<b>{query.data.replace('_', ' ').title()}</b> অপশনটি খুব শীঘ্রই আসছে!"
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='main_menu')]]
        await query.message.edit_text(text, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    keep_alive()
    
    TOKEN = os.getenv("BOT_TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    application.run_polling()
