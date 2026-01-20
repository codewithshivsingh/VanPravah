from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8085580303:AAHS3WzWToJi8eUvV02b90q-wCji5ldfkKc"

# ---------------- MAIN MENU ----------------
MAIN_MENU = [
    ["📋 General Enquiry", "📝 Register as Candidate"],
    ["📤 Upload Resume", "📢 Latest Job Openings"],
    ["🧾 Apply for a Job", "🎯 Interview Preparation"],
    ["🧭 Career Guidance", "🏢 Hiring for Companies"],
    ["💼 HR Consulting Services", "🏠 Work From Home Jobs"],
    ["🎓 Internship / Fresher Jobs"],
    ["☎️ Contact HR Team", "⭐ Feedback / Support"]
]

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 *Welcome to VanPravah HR Consultancy*\n\n"
        "We connect the right talent with the right opportunities.\n\n"
        "Please select an option from the menu below 👇"
    )

    reply_markup = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)

    await update.message.reply_text(
        welcome_text, reply_markup=reply_markup, parse_mode="Markdown"
    )

# ---------------- GENERAL ENQUIRY ----------------
async def general_enquiry_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📌 About Our Services"],
        ["⏰ Office Timings"],
        ["💰 Consultancy Charges"],
        ["📞 Talk to HR Executive"],
        ["🔙 Back to Main Menu"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "📋 *General Enquiry*\nChoose an option 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# ---------------- SUB-MENU HANDLER ----------------
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # ------------- GENERAL ENQUIRY ----------
    if text == "📋 General Enquiry":
        return await general_enquiry_menu(update, context)

    if text == "📌 About Our Services":
        return await update.message.reply_text(
            "💼 *Our Services*\n\n• Job placements\n• Resume shortlisting\n• Career guidance\n• Company hiring support",
            parse_mode="Markdown"
        )

    if text == "⏰ Office Timings":
        return await update.message.reply_text(
            "🕘 *Timing*: Mon–Sat • 10 AM – 6 PM", parse_mode="Markdown"
        )

    if text == "💰 Consultancy Charges":
        return await update.message.reply_text(
            "💰 Charges depend on profile.\nPlease contact HR for exact details.",
            parse_mode="Markdown"
        )

    if text == "📞 Talk to HR Executive":
        return await update.message.reply_text(
            "📞 Contact HR:\nPhone: +91-XXXXXXXXXX\nEmail: hr@vanpravah.com",
            parse_mode="Markdown"
        )

    # ----------- BACK TO MAIN MENU ----------
    if text == "🔙 Back to Main Menu":
        reply_markup = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
        return await update.message.reply_text(
            "🔙 Back to Main Menu", reply_markup=reply_markup
        )

    # ---------------- JOB OPENINGS ----------------
    if text == "📢 Latest Job Openings":
        keyboard = [
            ["💻 IT Jobs", "🏢 Non-IT Jobs"],
            ["🆕 Fresher Jobs", "🏠 Work From Home Jobs"],
            ["📍 Location Based Jobs"],
            ["🔙 Back to Main Menu"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        return await update.message.reply_text(
            "📢 *Latest Job Openings*\nChoose a category 👇",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    if text == "💻 IT Jobs":
        return await update.message.reply_text("💻 *Current IT Openings:*\n• Python Developer\n• Web Developer\n• QA Tester\n\nSend your resume.", parse_mode="Markdown")

    if text == "🏢 Non-IT Jobs":
        return await update.message.reply_text("🏢 *Non-IT Jobs:*\n• HR Executive\n• Telecaller\n• Sales Executive", parse_mode="Markdown")

    if text == "🆕 Fresher Jobs":
        return await update.message.reply_text("🆕 *Fresher Jobs Available*\n• BPO\n• Data Entry\n• Assistant Roles", parse_mode="Markdown")

    if text == "📍 Location Based Jobs":
        return await update.message.reply_text("📍 Mention your preferred location.", parse_mode="Markdown")

    # ---------------- UPLOAD RESUME ---------------
    if text == "📤 Upload Resume":
        return await update.message.reply_text(
            "📤 Please upload your resume (PDF/DOC).",
            parse_mode="Markdown"
        )

    # -------- RECEIVE RESUME FILE ----------
    if update.message.document:
        file = update.message.document
        await update.message.reply_text("📥 Resume uploaded successfully!\nHR team will contact you soon.")
        return await context.bot.send_document(
            chat_id=YOUR_TELEGRAM_ID,  # <-- apna Telegram ID yahan daalna
            document=file.file_id,
            caption=f"New Resume from @{update.message.from_user.username}"
        )

    # ---------------- REGISTER AS CANDIDATE ---------------
    if text == "📝 Register as Candidate":
        return await update.message.reply_text(
            "📝 Send your details in this format:\n\nName:\nAge:\nExperience:\nLocation:\nPreferred Job:\nPhone:",
            parse_mode="Markdown"
        )

    # ---------------- INTERVIEW PREP ----------------
    if text == "🎯 Interview Preparation":
        return await update.message.reply_text(
            "🎯 *Interview Tips:*\n• Be confident\n• Know your resume\n• Research the company\n• Prepare common questions",
            parse_mode="Markdown"
        )

    # ---------------- CAREER GUIDANCE ----------------
    if text == "🧭 Career Guidance":
        return await update.message.reply_text(
            "🧭 Share your education + experience.\nOur team will guide you.",
            parse_mode="Markdown"
        )

    # ---------------- HIRING FOR COMPANIES ----------------
    if text == "🏢 Hiring for Companies":
        return await update.message.reply_text(
            "🏢 *Employer Form*\n\nSend this:\nCompany Name:\nPosition:\nExperience Required:\nSalary Range:\nLocation:\nContact Person:",
            parse_mode="Markdown"
        )

    # ---------------- CONTACT HR ----------------
    if text == "☎️ Contact HR Team":
        return await update.message.reply_text(
            "☎️ *HR Contact*\nPhone: +91-XXXXXXXXXX\nEmail: hr@vanpravah.com",
            parse_mode="Markdown"
        )

    # ---------------- FEEDBACK ----------------
    if text == "⭐ Feedback / Support":
        return await update.message.reply_text(
            "⭐ Please share your feedback.\nWe appreciate your input.",
            parse_mode="Markdown"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, menu_handler))

print("VanPravah HR Bot Running...")
app.run_polling()


