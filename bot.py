from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ===== Handler Perintah Instagram Pembalap =====
async def alex(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Alex Albon: https://www.instagram.com/alex_albon?igsh=MzRxeGV0dGdyNzI0")

async def carlos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Carlos Sainz: https://www.instagram.com/carlossainz55?igsh=ZjJmZXR4ejczYXl6")

async def sainzhq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fanpage CarlosSainzHQ: https://www.instagram.com/carlossainzhq?igsh=ODd5NzhpeDdhcWsz")

async def sainznews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fanpage SainzNews: https://www.instagram.com/sainznews?igsh=MWdndGcwMDAzb2Fkag==")

# ===== Handler Perintah Instagram Media =====
async def f1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Formula 1: https://www.instagram.com/f1?igsh=MXEzMW4zb3g4YzkzeQ==")

async def scuderia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Scuderia Ferrari: https://www.instagram.com/scuderiaferrari?igsh=dGU0cHdzbDMyMHBj")

async def williams(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Williams Racing: https://www.instagram.com/williamsracing?igsh=b3piazFwYTdlMjFq")

# ===== Handler Website Berita F1 =====
async def formula1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Website Formula1.com: https://www.formula1.com/")

async def autosport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Website Autosport.com: https://www.autosport.com/")

async def planetf1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Website PlanetF1.com: https://www.planetf1.com/")

# ===== Handler Stiker dari Foto Reply =====
async def sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message and update.message.reply_to_message.photo:
        photo = update.message.reply_to_message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=file.file_id)
    else:
        await update.message.reply_text("Balas foto dulu, lalu kirim /stiker untuk mengubah jadi stiker!")

# ===== Start dan Chat Auto Reply Sederhana =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo, aku bot info F1! Ketik /carlos, /alex, /f1, /scuderia, dll!")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text.lower()
    if "carlos" in pesan:
        await update.message.reply_text("Carlos Sainz memang keren banget ya!")
    elif "alex" in pesan:
        await update.message.reply_text("Alex Albon makin tajam musim ini!")
    elif "f1" in pesan:
        await update.message.reply_text("Kamu suka nonton F1 juga? Sama dong!")
    else:
        await update.message.reply_text("Aku belum ngerti itu, tapi aku senang kamu chat aku 🥰")

# ===== Main Bot Setup =====
if __name__ == "__main__":
    app = ApplicationBuilder().token("7971477993:AAEW9JqSHj3WvnOtUhdgj3QeaI_qMKaW1Bg").build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("alex", alex))
    app.add_handler(CommandHandler("carlos", carlos))
    app.add_handler(CommandHandler("sainzhq", sainzhq))
    app.add_handler(CommandHandler("sainznews", sainznews))
    app.add_handler(CommandHandler("f1", f1))
    app.add_handler(CommandHandler("scuderia", scuderia))
    app.add_handler(CommandHandler("williams", williams))
    app.add_handler(CommandHandler("formula1", formula1))
    app.add_handler(CommandHandler("autosport", autosport))
    app.add_handler(CommandHandler("planetf1", planetf1))
    app.add_handler(CommandHandler("stiker", sticker))

    # Auto Reply Chat Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot aktif...")
    app.run_polling()
