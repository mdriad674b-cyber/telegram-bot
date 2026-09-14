from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = '7993052115:AAGM58l-JJfaAU7nD8ho80_PKuU8haLGFIA'
ADMIN_ID = 8995171689 # ⚠️ এখানে আপনার Telegram Numeric ID দিন (@userinfobot থেকে পাবেন)
PAYMENT_NUMBER = "01998307838"  # ⚠️ আপনার বিকাশ/নগদ নম্বর

WAITING_TRX = 1

# ১. মেনু সার্ভিসেস
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "◈────────────◈\n"
        "🎮 *MURUBBI X SHOP* 🎮\n"
        "◈────────────◈\n\n"
        "Hey, glad to have you here.\n\n"
        "*যা যা পাচ্ছেন এখানে:*\n"
        "▸ 🔑 Premium Game Keys\n"
        "▸ ⚡ Instant 24/7 Delivery\n"
        "▸ 🔒 100% Secure Payment\n"
        "▸ 💸 Best Price Guarantee\n"
        "▸ 🎁 Referral Rewards\n"
        "▸ 🏆 Real Human Support\n\n"
        "◈────────────◈\n"
        "👇 *নিচ থেকে শুরু করুন*"
    )
    
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop Now", callback_data='shop_now')],
        [InlineKeyboardButton("👤 Profile", callback_data='profile'), InlineKeyboardButton("🎯 FF Likes", callback_data='ff_likes')],
        [InlineKeyboardButton("💵 Add Balance", callback_data='add_balance'), InlineKeyboardButton("🎁 Referral", callback_data='referral')],
        [InlineKeyboardButton("🎰 Lucky Spin", callback_data='spin'), InlineKeyboardButton("📁 Files", callback_data='files')],
        [InlineKeyboardButton("📺 Tutorials", callback_data='tutorials'), InlineKeyboardButton("🎫 Support", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)
    else:
        await update.callback_query.message.edit_text(text, parse_mode='Markdown', reply_markup=reply_markup)
    return ConversationHandler.END

# ২. প্রোডাক্ট ক্যাটালগ (Shop Now)
async def shop_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    text = (
        "🎮 *CHOOSE YOUR GAME*\n"
        "◈────────────◈\n\n"
        "⭐ *Available Products*\n\n"
        "⚔️ Premium Keys\n"
        "⚡ Instant Delivery\n"
        "🔒 Secure Payment\n"
        "🏆 24/7 Support\n\n"
        "📦 *Select a product below:*"
    )
    keyboard = [
        [InlineKeyboardButton("🛒 FF GUILD GLORY", callback_data='prod_drip')],
        [InlineKeyboardButton("🛒 DRIP WIRE ANDROID", callback_data='prod_drip')],
        [InlineKeyboardButton("🛒 BALA MOD", callback_data='prod_drip')],
        [InlineKeyboardButton("🛒 DRIP CLIENT PROXY", callback_data='prod_drip')],
        [InlineKeyboardButton("🛒 XREG ANDROID+IOS", callback_data='prod_drip')],
        [InlineKeyboardButton("🛒 BRMOD PC", callback_data='prod_drip')],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data='main_menu')]
    ]
    await query.message.edit_text(text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    return ConversationHandler.END

# ৩. প্ল্যান সিলেক্ট (DRIP WIRE ANDROID)
async def product_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    file_link = "[https://t.me/your_file_link](https://t.me/your_file_link)"
    text = (
        "🛒 *DRIP WIRE ANDROID*\n\n"
        "📊 *STOCK & PRICING:*\n"
        "◈────────────◈\n\n"
        "*6 Hours*\n📦 Stock: ✅ In Stock\n💰 Price: ৳50\n\n"
        "*12 Hours*\n📦 Stock: ✅ In Stock\n💰 Price: ৳90\n\n"
        "*1 Day*\n📦 Stock: ✅ In Stock\n💰 Price: ৳150\n\n"
        "*7 Days*\n📦 Stock: ✅ In Stock\n💰 Price: ৳500\n\n"
        "🎯 *SELECT YOUR PLAN:*"
    )
    keyboard = [
        [InlineKeyboardButton("🛒 Buy 6 Hours - ৳50", callback_data='buy_6h')],
        [InlineKeyboardButton("🛒 Buy 12 Hours - ৳90", callback_data='buy_12h')],
        [InlineKeyboardButton("🛒 Buy 1 Day - ৳150", callback_data='buy_1d')],
        [InlineKeyboardButton("🛒 Buy 7 Days - ৳500", callback_data='buy_7d')],
        [InlineKeyboardButton("🎥 Demo", url='https://murubbixtopup.com/')],
        [InlineKeyboardButton("⬅️ Back to Shop", callback_data='shop_now')]
    ]
    await query.message.edit_text(text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    return ConversationHandler.END

# ৪. পেমেন্ট নির্দেশিকা ও TrxID গ্রহণ
async def process_buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    plans = {
        'buy_6h': ('6 Hours', '৳50'),
        'buy_12h': ('12 Hours', '৳90'),
        'buy_1d': ('1 Day', '৳150'),
        'buy_7d': ('7 Days', '৳500')
    }
    plan_name, price = plans.get(query.data, ('Selected Plan', '৳0'))
    context.user_data['selected_plan'] = f"{plan_name} ({price})"
    
    text = (
        f"💳 *পেমেন্ট নির্দেশিকা ({plan_name})*\n\n"
        f"আপনার সিলেক্ট করা মূল্য: *{price}*\n\n"
        f"১. বিকাশ / নগদ (Send Money/Cashout): `{PAYMENT_NUMBER}`\n"
        f"২. টাকা পাঠিয়ে আপনার **TrxID** বা **প্রেরকের নম্বরটি** নিচে লিখে মেসেজ দিন।"
    )
    await query.message.reply_text(text, parse_mode='Markdown')
    return WAITING_TRX

# ৫. কাস্টমারের দেওয়া TrxID এডমিনের কাছে পাঠানো
async def receive_trx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    trx_text = update.message.text
    plan = context.user_data.get('selected_plan', 'Unknown Plan')
    
    # এডমিন মেসেজ
    admin_msg = (
        f"🚨 *নতুন অর্ডার এসেছে!*\n\n"
        f"👤 কাস্টমার: {user.first_name} (@{user.username})\n"
        f"🆔 User ID: `{user.id}`\n"
        f"📦 প্ল্যান: {plan}\n"
        f"🧾 TrxID / নম্বর: `{trx_text}`"
    )
    
    keyboard = [
        [
            InlineKeyboardButton("✅ Approve Order", callback_data=f"app_{user.id}"),
            InlineKeyboardButton("❌ Reject Order", callback_data=f"rej_{user.id}")
        ]
    ]
    
    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_msg, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    await update.message.reply_text("✅ আপনার পেমেন্ট তথ্য জমা নেওয়া হয়েছে! এডমিন ভেরিফাই করে ফাইল পাঠাবে।")
    return ConversationHandler.END

# ৬. এডমিনের একশন (Approve/Reject)
async def admin_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    user_id = int(data.split('_')[1])
    
    if data.startswith("app_"):
        file_link = "https://t.me/your_file_link"  # ⚠️ এখানে কাস্টমারকে দেওয়ার জন্য প্যানেল ফাইল বা কি (Key) লিঙ্ক দিন
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🎉 *আপনার পেমেন্ট ভেরিফাই হয়েছে!*\n\nএখানে আপনার প্যানেল ফাইল/কী (Key):\n{file_link}",
            parse_mode='Markdown'
        )
        await query.message.edit_text(query.message.text + "\n\n✅ *Status: APPROVED*")
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text="❌ আপনার পেমেন্ট ভেরিফিকেশন ব্যর্থ হয়েছে। সঠিক TrxID দিয়ে আবার চেষ্টা করুন বা সাপোর্ট হেল্প নিন।"
        )
        await query.message.edit_text(query.message.text + "\n\n❌ *Status: REJECTED*")

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(process_buy, pattern='^buy_')],
        states={
            WAITING_TRX: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_trx)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(shop_menu, pattern='^shop_now$'))
    app.add_handler(CallbackQueryHandler(start, pattern='^main_menu$'))
    app.add_handler(CallbackQueryHandler(product_detail, pattern='^prod_drip$'))
    app.add_handler(CallbackQueryHandler(admin_action, pattern='^(app_|rej_)'))
    app.add_handler(conv_handler)
    
    print("Bot starting...")
    app.run_polling()

if __name__ == '__main__':
    main()