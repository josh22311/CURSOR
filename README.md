# 🔥 TELEGRAM BOT - RENDER DEPLOYMENT 🔥

YO! This is your SICK Telegram bot that shows uptime and stats! 💪

## 🚀 Features

✅ **Uptime Tracking** - See how long the bot's been running  
✅ **Status Command** - Check bot health with `/status`  
✅ **Ping Command** - Test response time with `/ping`  
✅ **Stats Command** - Detailed statistics with `/stats`  
✅ **Help Command** - Get all commands with `/help`  

## 📋 Available Commands

- `/start` - Welcome message 👋
- `/status` - Bot status & uptime ⏰
- `/ping` - Test response time 🏓
- `/stats` - Detailed statistics 📊
- `/help` - Show help message 📖

## 🔧 Local Testing (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

## 🚀 DEPLOY TO RENDER

### Method 1: Via Render Dashboard (EASIEST!)

1. **Push to GitHub** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Telegram bot"
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```

2. **Go to Render Dashboard**: https://dashboard.render.com/

3. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Select this repository

4. **Configure Service**:
   - **Name**: `telegram-bot` (or whatever you want)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: Free

5. **Add Environment Variable**:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: `8465562265:AAHXkLGY_E2FNpNXX9fvtYRcFTd5tG3wCB0`

6. **Deploy**: Click "Create Web Service"

### Method 2: Via Render CLI

```bash
# Install Render CLI
npm install -g render-cli

# Login (you'll provide token when ready)
render login

# Deploy
render deploy
```

## 🎯 After Deployment

Once deployed on Render:
1. Open Telegram
2. Search for your bot
3. Type `/start` to wake it up! 🔥
4. Type `/status` to see uptime! ⏰

## 🔥 IMPORTANT NOTES

- **Free Tier**: Render free tier spins down after 15 min of inactivity
- **First Request**: Might take 30-60 seconds to wake up (cold start)
- **Uptime Resets**: When Render restarts the service
- **Token Security**: NEVER commit tokens to GitHub (use environment variables!)

## 🐛 Troubleshooting

**Bot not responding?**
- Check Render logs: Dashboard → Your Service → Logs
- Make sure environment variable is set
- Verify bot token is correct

**Bot keeps sleeping?**
- Free tier limitation - consider upgrading to paid tier
- Or use a cron job to ping it every 10 minutes

## 💪 TECH STACK

- **Language**: Python 3.11+
- **Library**: python-telegram-bot 20.7
- **Platform**: Render
- **Architecture**: Long polling (no webhooks needed!)

## 🎉 THAT'S IT BRO!

Your bot is READY TO GO! Just deploy it and you're SET! 🚀

Questions? Just ask! I GOT YOU! 💪😎
