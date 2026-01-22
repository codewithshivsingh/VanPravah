import os
from keep_alive import keep_alive
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# -----------------------------
#        START COMMAND
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["General Enquiry", "Register as Candidate"],
        ["Upload Resume", "Latest Job Openings"],
        ["Apply for a Job", "Interview Preparation"],
        ["Career Guidance", "Hiring for Companies"],
        ["Contact HR Team", "Feedback / Support"]
    ]

    await update.message.reply_text(
        "Welcome to *VanPravah Solutions Bot* \n"
        "How can we help you today?",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# -----------------------------
#       MESSAGE HANDLER
# -----------------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "General Enquiry":
        await update.message.reply_text(
            "Thank you for your enquiry.\n"
            "Our HR team will contact you shortly.\n\n"
            "Please select another option from the menu."
        )

    elif text == "Register as Candidate":
        await update.message.reply_text(
            "Please share the following details:\n"
            "1. Full Name\n"
            "2. Email ID\n"
            "3. Phone Number\n"
            "4. Location\n"
            "5. Highest Qualification"
        )

    elif text == "Upload Resume":
        await update.message.reply_text("Please upload your resume in PDF format.")

    elif text == "Latest Job Openings":
        await update.message.reply_text(
            "Our latest job openings:\n"
            "• HR Executive\n"
            "• Sales Associate\n"
            "• Data Entry Operator\n"
            "• Front Desk Coordinator\n"
            "• Digital Marketing Assistant\n\n"
            "Apply now by selecting *Apply for a Job*."
        )

    elif text == "Apply for a Job":
        await update.message.reply_text("Please send the job title you want to apply for.")

    elif text == "Interview Preparation":
        await update.message.reply_text(
            "We provide interview guidance, mock tests and grooming support.\n"
            "Our team will contact you for further assistance."
        )

    elif text == "Career Guidance":
        await update.message.reply_text(
            "Please share your qualification & work experience.\n"
            "Our expert will guide you with the best career options."
        )

    elif text == "Hiring for Companies":
        await update.message.reply_text(
            "Please share your company name, role requirements and location.\n"
            "Our HR team will contact you soon."
        )

    elif text == "Contact HR Team":
        await update.message.reply_text(
            "You can reach our HR team at:\n"
            " hr@vanpravahsolutions.com\n"
            " +91-9876543210"
        )

    elif text == "Feedback / Support":
        await update.message.reply_text(
            "Please share your feedback or issue.\n"
            "Our team will assist you shortly."
        )

    else:
        await update.message.reply_text(
            "Thank you for your message.\n"
            "Please select an option from the menu."
        )

# -----------------------------
#        RESUME HANDLER
# -----------------------------
async def handle_resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    if file.mime_type == "application/pdf":
        await update.message.reply_text("Resume received successfully! \nWe will review and contact you soon.")
    else:
        await update.message.reply_text("Please upload your resume in PDF format only.")

# -----------------------------
#      MAIN FUNCTION
# -----------------------------
def main():
    # Token check
    BOT_TOKEN = os.getenv("TOKEN")
    
    if not BOT_TOKEN:
        print("Error: TOKEN not found in Environment Variables!")
        return

    # Build the application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_resume))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("BOT STARTED... ")
    
    # Run Polling (Isme 'asyncio.run' ki zarurat nahi hoti)
    app.run_polling()

if __name__ == "__main__":
    keep_alive()  # Web server start
    main()        # Bot start
