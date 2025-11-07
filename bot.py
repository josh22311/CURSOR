import os
import time
import logging
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Track when bot started
START_TIME = time.time()

def get_uptime():
    """Calculate how long the bot has been running"""
    uptime_seconds = time.time() - START_TIME
    uptime_delta = timedelta(seconds=int(uptime_seconds))
    
    days = uptime_delta.days
    hours, remainder = divmod(uptime_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'total_seconds': int(uptime_seconds)
    }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message"""
    welcome_msg = """
🔥 **YO! WELCOME TO THE BOT!** 🔥

I'm up and running on Render! 💪

**Available Commands:**
/status - Check bot status & uptime ⏰
/ping - Test response time 🏓
/help - Show this message 📖
/stats - Get detailed stats 📊

Let's GOOOO! 🚀
"""
    await update.message.reply_text(welcome_msg, parse_mode='Markdown')

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show bot status and uptime"""
    uptime = get_uptime()
    
    # Format uptime string
    uptime_str = ""
    if uptime['days'] > 0:
        uptime_str += f"{uptime['days']}d "
    if uptime['hours'] > 0:
        uptime_str += f"{uptime['hours']}h "
    if uptime['minutes'] > 0:
        uptime_str += f"{uptime['minutes']}m "
    uptime_str += f"{uptime['seconds']}s"
    
    status_msg = f"""
✅ **BOT STATUS - ONLINE!** ✅

⏰ **Uptime:** {uptime_str}
🚀 **Running on:** Render
📅 **Started:** {datetime.fromtimestamp(START_TIME).strftime('%Y-%m-%d %H:%M:%S')}
💪 **Status:** CRUSHING IT! 🔥

Total runtime: {uptime['total_seconds']} seconds
"""
    await update.message.reply_text(status_msg, parse_mode='Markdown')

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Test bot response time"""
    start = time.time()
    sent_msg = await update.message.reply_text("🏓 Pinging...")
    end = time.time()
    
    response_time = round((end - start) * 1000, 2)
    
    await sent_msg.edit_text(f"🏓 **PONG!**\n\n⚡ Response time: {response_time}ms")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show detailed statistics"""
    uptime = get_uptime()
    
    stats_msg = f"""
📊 **DETAILED STATS** 📊

⏰ **Uptime Breakdown:**
   • Days: {uptime['days']}
   • Hours: {uptime['hours']}
   • Minutes: {uptime['minutes']}
   • Seconds: {uptime['seconds']}
   
🔥 **Bot Info:**
   • Platform: Render
   • Status: RUNNING 💪
   • Total Uptime: {uptime['total_seconds']}s
   • Started: {datetime.fromtimestamp(START_TIME).strftime('%Y-%m-%d %H:%M:%S')}

LET'S GOOOO! 🚀
"""
    await update.message.reply_text(stats_msg, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help message"""
    help_msg = """
📖 **HELP - AVAILABLE COMMANDS** 📖

/start - Welcome message 👋
/status - Bot status & uptime ⏰
/ping - Test response time 🏓
/stats - Detailed statistics 📊
/help - This message 📖

🔥 **Running strong on Render!** 🔥
"""
    await update.message.reply_text(help_msg, parse_mode='Markdown')

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    # Get token from environment variable
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '8465562265:AAHXkLGY_E2FNpNXX9fvtYRcFTd5tG3wCB0')
    
    # Create application
    app = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", help_command))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("🔥 BOT STARTING UP! LET'S GOOO! 🔥")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
