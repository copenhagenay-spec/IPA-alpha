# VERA — Voice Enabled Response Assistant

Offline personal voice assistant for Windows. No cloud required — everything runs locally.

## Quick Start

1. Install Python 3.11+ from [python.org](https://www.python.org/downloads/) — check **"Add Python to PATH"**
2. Double-click `setup.cmd` to install dependencies (one-time, ~310MB)
3. Double-click `run_ipa.vbs` to launch (no terminal window)
4. The setup wizard opens on first run — follow the steps to configure your listening mode

## Listening Modes

| Mode | How it works |
|---|---|
| **Hold-to-talk** | Hold a key while speaking, release to process |
| **Toggle-to-talk** | Press once to start, press again to stop |
| **Wake word** | Say "vera" to activate, then speak your command |

## Voice Commands

Say `what can I say` at any time to hear all available commands.

| Category | Examples |
|---|---|
| Apps | `open spotify`, `close discord` |
| Search | `search for <query>`, `youtube <query>` |
| Media | `play`, `pause`, `skip`, `volume up`, `mute` |
| Timers | `set a timer 5 minutes`, `cancel timer` |
| Notes | `note <text>`, `open notes`, `delete last note` |
| Clipboard | `copy that`, `read clipboard`, `clear clipboard` |
| TTS | `read out <text>` — speaks text aloud (routes to Discord mic if Voice Output is set) |
| Key Binds | `reload` → presses R (configured in Actions tab) |
| Discord | `discord <channel> <message>`, `discord <server> <channel> <message>` |
| System | `sleep computer`, `restart assistant` |
| Conversation | `tell me a joke`, `what's your name`, `good morning` |

> **Note:** Key binds may be blocked by anti-cheat software (EAC/BattlEye) in protected games.

## Discord

VERA can send messages to Discord channels via webhooks and read the last message using a bot token. Multi-server support — add servers with nicknames and use `discord <server> <channel> <message>`.

See the [Discord Setup Guide](docs/discord.md) for full instructions.

## Mishear Training

Go to the **Training** tab to correct phrases VERA didn't understand. See [Mishear Training](docs/training.md) for details.

## AI Setup (Optional)

The `ask <question>` command supports on-demand AI responses.

| Provider | Key prefix | Notes |
|---|---|---|
| Groq | `gsk_` | Free — 14,400 requests/day |
| OpenAI | `sk-` | Paid — gpt-4o-mini |
| Anthropic | `sk-ant-` | Paid — Claude Haiku |

Paste your key in the **Integrations** tab → AI API Key field.

## UI

- Notifications appear inline — no popups
- Unsaved changes are indicated in the title bar
- Key recording happens inside the window — no separate dialog

## Troubleshooting

- **Nothing transcribed** — check Windows microphone permissions and input device
- **App won't open** — run `run_ipa.cmd` directly to see errors in the terminal
- **Command not triggering** — check **Last Transcript** in the UI, add a mishear correction in the Training tab
- **Crash logs** — saved to `data/logs/assistant.log`

## Uninstall

Double-click `uninstall.cmd` or use Add/Remove Programs. Your settings and memory are preserved.
