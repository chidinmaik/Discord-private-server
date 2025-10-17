# 📨 JoinNotifier — Private Discord Join Notification Bot

A simple but powerful **Discord bot built with Python and discord.py** that quietly sends **private DM notifications** to the bot owner whenever a new user joins *any server* the bot is in.  

It sends **no messages in public channels**, making it perfect for personal use or silent monitoring.

---

## 🚀 Features
- 📩 Sends a **direct message** (DM) to the bot owner when a new member joins a server.
- 🧾 The DM includes:
  - Username and ID  
  - Server name  
  - Join time (UTC)  
  - Avatar thumbnail  
- 🕵️‍♂️ Works silently — no server messages or commands needed.  
- 🧠 Lightweight: runs smoothly on **Replit’s free tier**.  
- 🔒 Secure: token & ID stored safely in Replit **Secrets (Environment Variables)**.

---

## 🧰 Project Structure
main.py # Bot source code
requirements.txt # Python dependencies
README.md # This file
.gitignore # Files to ignore in git (e.g., secrets)


---

## 🧑‍💻 Prerequisites
- A **Discord account**
- **Python 3.10+** (if running locally) or **Replit** account (free)
- A **Discord Developer Portal** app with a bot created

---

## ⚙️ Step 1: Create Your Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **“New Application”**, give it a name (e.g., `JoinNotifier`), and click **Create**.
3. In the sidebar, click **Bot** → **Add Bot**.
4. Scroll down to **Privileged Gateway Intents** and enable:
   - ✅ Server Members Intent
5. Click **Save Changes**.
6. Copy your **Bot Token** (you’ll add it later to Replit).
7. Copy your **Client ID** from the **General Information** tab.

---

## ⚙️ Step 2: Get Your Discord User ID
1. In Discord, go to **User Settings → Advanced → Enable Developer Mode.**
2. Right-click your username → click **Copy ID**.  
   This is your **OWNER_ID**.

---

## ☁️ Step 3: Set Up on Replit (Free Hosting)
1. Go to [https://replit.com](https://replit.com) and create an account.  
2. Click **“+ Create” → “Python”** Repl.  
3. Copy your project files into the Replit editor (`main.py`, `requirements.txt`, `README.md`, `.gitignore`).
4. On the left menu, click **“Tools → Secrets (Environment Variables)”** and add:
   - `DISCORD_TOKEN` → your bot token  
   - `OWNER_ID` → your numeric Discord user ID
5. Click the green **Run** button.  
   You should see:

✅ Logged in as JoinNotifier (ID: 123456789012345678)
Bot is online and ready!




---

## 🔗 Step 4: Invite the Bot to a Server
Use this invite link format:



https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=0




Replace `YOUR_CLIENT_ID` with your bot’s client ID.

✅ It uses **no permissions** — totally silent and safe to invite anywhere.

---

## 💬 Step 5: Test It
1. Invite the bot to your server using the link above.  
2. Have a new member join the server.  
3. Check your **DMs** — you should receive an embed like this:

> **📢 New Member Joined!**  
> 👤 Username: `JohnDoe#1234`  
> 🏠 Server: `Cool Server`  
> ⏰ Joined: `2025-10-17 13:07:55 (UTC)`  
> 🆔 ID: `123456789012345678`

---

## 🕒 Keep It Running (Optional)
Replit free accounts sleep after some inactivity.

To keep your bot alive 24/7:
1. Visit [https://uptimerobot.com/](https://uptimerobot.com/)
2. Create a **free account**
3. Add a new **HTTP monitor**
4. Paste your Replit web URL (shown in console like `https://yourname.repl.co`)
5. Set it to ping every 5 minutes

Now your bot will stay online continuously!

---

## 🧩 Troubleshooting

| Problem | Fix |
|----------|------|
| ❌ Bot offline | Replit stopped — click **Run** again |
| ⚠️ No DMs received | Ensure **Server Members Intent** is ON |
| 🚫 DM failed (403) | Turn on “Allow DMs from server members” |
| 🔐 Invalid token | Reset token in Developer Portal & update in Secrets |
| 🕵️‍♂️ No join alerts | Bot must already be in the server before the join event |

---

## 🧱 Contributing
Pull requests are welcome!  
If you’d like to improve or extend the bot:
1. Fork this repo  
2. Create a branch: `git checkout -b feature-name`
3. Commit your changes
4. Push and open a Pull Request 🚀

Please **never commit secrets or tokens**.

---

## 🔒 Security
- Keep your **bot token** private.
- Never hardcode secrets in your code or README.
- If your token leaks, **reset it immediately** from the Discord Developer Portal.

---

## 🧾 License
This project is open-source under the [MIT License](LICENSE).

---

## 👤 Author
Built with ❤️ by   JEDI_DTECHMAKER — inspired by Discord automation for beginners in Nigeria 🇳🇬  
Feel free to fork, remix, and share!

---

