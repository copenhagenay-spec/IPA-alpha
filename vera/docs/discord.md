# Discord Setup Guide

VERA can send messages to Discord channels by voice using webhooks, and read the last message in a channel using a Discord bot. Multi-server support lets you manage channels across different servers with nicknames.

---

## Commands

| What to say | What happens |
|---|---|
| `discord <channel> <message>` | Sends a message to a channel |
| `discord <server> <channel> <message>` | Sends to a specific server's channel |
| `read discord <channel>` | Reads the last message in a channel aloud |
| `read discord <server> <channel>` | Reads from a specific server's channel |
| `discord delete <channel>` | Deletes the last message in a channel |
| `discord purge <channel> <n>` | Bulk deletes up to 100 messages |

> **Example:** "discord baddie general hey guys" — sends "hey guys" to the general channel on the server nicknamed "baddie"

---

## Step 1 — Create a Webhook

For each channel you want VERA to send messages to:

1. Open Discord and go to your server
2. Right-click the channel → **Edit Channel**
3. Go to the **Integrations** tab
4. Click **Webhooks** → **New Webhook**
5. Give it a name (e.g. "VERA") and click **Copy Webhook URL**
6. Click **Save**

---

## Step 2 — Add a Server (for multi-server support)

If you use multiple Discord servers or want to use the `discord <server> <channel>` command format:

1. Open VERA and go to the **Discord** tab
2. Under **Servers**, enter a **Nickname** (e.g. `baddie`) and the **Server ID**
3. Click **Add Server**

**To get your Server ID:**
1. Open Discord → **User Settings** → **Advanced** → enable **Developer Mode**
2. Right-click your server icon → **Copy Server ID**

> If you only use one server, you can skip this step — the single-server commands still work without adding a server entry.

---

## Step 3 — Add Channels

1. In the **Discord** tab, go to the **Channels** section
2. Enter the **Channel name** (e.g. `general`)
3. Optionally enter the **Server nickname** to tie this channel to a specific server (e.g. `baddie`)
4. Paste the **Webhook URL** you copied in Step 1
5. Click **Add Channel**
6. Click **Save Config**

---

## Step 4 — Bot Token (for Read Discord)

Reading messages requires a Discord bot. This is optional — sending via webhook works without it.

**Create a bot:**
1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **New Application** → give it a name
3. Go to the **Bot** tab → click **Add Bot**
4. Under **Token** click **Copy**
5. Paste it into the **Bot Token** field in VERA's Discord tab
6. Add the bot to your server via OAuth2 → Bot scope with **Read Messages** permission

**Add Server ID for reading:**
- Enter your server's ID in the **Default Server ID** field (or add it via the Servers list with a nickname)

> ⚠️ Your bot token grants full access to your bot — treat it like a password. Never share it publicly or commit it to a repository. If it's ever leaked, reset it immediately in the Discord Developer Portal.

---

## Voice Output (Discord TTS Mic)

VERA can route the `read out <text>` command through a virtual microphone so Discord picks it up as your mic input — useful if you want to speak through Discord without using your real mic.

**Setup:**
1. Download and install **VB-Cable** (free) from [vb-audio.com/Cable](https://vb-audio.com/Cable)
2. Reboot after install
3. In VERA → **Settings** → **Voice Output** → select **CABLE Input (VB-Audio Virtual Cable)**
4. In Discord → **User Settings** → **Voice & Video** → set **Input Device** to **CABLE Output**
5. Say `read out hey guys` — it will play through Discord

> All other VERA responses (confirmations, fallback, etc.) still play through your speakers. Only `read out` routes to the virtual mic.

---

## Troubleshooting

**"Message failed to send"**
- Check your webhook URL is correct and hasn't been deleted
- Make sure you have an active internet connection

**"Read discord isn't working"**
- Make sure your bot token is entered and saved
- Verify the Server ID is correct
- The bot must be a member of your server with Read Messages permission

**"Wrong server"**
- If you have channels with the same name on different servers, use the server nickname: `discord baddie general hey`
