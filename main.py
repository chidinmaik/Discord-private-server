# main.py
import os
import asyncio
from datetime import datetime, timezone

import discord
from discord.ext import commands

# --- Configuration from environment variables (see Replit secrets instructions below) ---
TOKEN = os.getenv("DISCORD_TOKEN")      # your bot token (keep secret!)
OWNER_ID = int(os.getenv("OWNER_ID", "0"))  # your Discord user ID (the recipient of notifications)
# -------------------------------------------------------------------------

intents = discord.Intents.default()
intents.members = True  # required to receive on_member_join events

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Optional: simple logger
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("join-notifier")

@bot.event
async def on_ready():
    logger.info(f"Bot ready. Logged in as {bot.user} (ID: {bot.user.id})")
    # Pre-fetch owner user to ensure fetch permissions early (not strictly necessary)
    try:
        owner = await bot.fetch_user(OWNER_ID)
        logger.info(f"Notification target set to {owner} (ID: {OWNER_ID})")
    except Exception:
        logger.warning("Could not fetch OWNER_ID at startup. Will fetch on events.")

@bot.event
async def on_member_join(member: discord.Member):
    """
    Called when a member joins a guild the bot is in.
    We build an embed with member info and DM it to OWNER_ID.
    """
    try:
        guild = member.guild
        # Prefer member.joined_at when available, otherwise use now (UTC)
        join_time = member.joined_at
        if join_time is None:
            join_time = datetime.now(timezone.utc)
        # Build embed
        embed = discord.Embed(
            title="New user joined a server",
            description=f"A new member joined **{guild.name}**.",
            timestamp=join_time,
            color=discord.Color.blurple()
        )
        embed.add_field(name="User", value=f"{member} (display name)", inline=True)
        embed.add_field(name="User ID", value=str(member.id), inline=True)
        embed.add_field(name="Server", value=f"{guild.name}\nID: {guild.id}", inline=False)
        embed.set_author(name=str(member), icon_url=member.display_avatar.url if member.display_avatar else None)
        embed.set_thumbnail(url=member.display_avatar.url if member.display_avatar else None)
        embed.set_footer(text="Member join time (UTC)")
        # Attempt to fetch owner (fresh)
        owner = await bot.fetch_user(OWNER_ID)
        # Send embed via DM
        try:
            await owner.send(embed=embed)
            logger.info(f"Sent join notification for {member} in {guild.name} to {owner}.")
        except discord.Forbidden:
            logger.warning("Could not send DM to owner: Forbidden (they may have DMs disabled).")
        except Exception as e:
            logger.exception("Failed to send DM to owner: %s", e)
    except Exception as exc:
        logger.exception("Error in on_member_join handler: %s", exc)


# ---- Small heartbeat webserver used for keepalive pings (Replit + UptimeRobot trick) ----
# If you don't want keepalive, you may remove the webserver section. Keepalive doesn't affect bot logic.
def start_keepalive():
    try:
        from flask import Flask
        app = Flask("keepalive")

        @app.route("/")
        def home():
            return "OK", 200

        from threading import Thread
        def run():
            app.run(host="0.0.0.0", port=int(os.getenv("PORT", 3000)))  # Replit provides $PORT
        t = Thread(target=run, daemon=True)
        t.start()
        logger.info("Keepalive webserver started.")
    except Exception:
        logger.warning("Flask not installed: keepalive server not started. Install Flask if you want a keepalive page.")

if __name__ == "__main__":
    # Start keepalive webserver (optional)
    start_keepalive()
    # Run bot
    if TOKEN is None or OWNER_ID == 0:
        logger.error("Missing DISCORD_TOKEN or OWNER_ID. Please set them as environment variables.")
        raise SystemExit("Missing configuration")
    bot.run(TOKEN)
