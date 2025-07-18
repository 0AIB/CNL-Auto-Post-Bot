Here’s the README.md code (in Markdown format) for your CNL-Auto-Post-Bot Telegram bot that auto-forwards channel messages using MongoDB and a bot token:


---

# CNL-Auto-Post-Bot

A simple Telegram bot that automatically forwards new messages from one channel to another. You can configure multiple independent channel pairs like:

- Channel1 → Channel2  
- Channel3 → Channel4

> ❌ You **cannot** do chained forwarding like Channel1 → Channel2 → Channel3.

---

## ✅ Features

- Forward posts automatically from one channel to another.
- Supports multiple source → destination mappings.
- Admin commands to manage mappings.
- Built using Pyrogram + MongoDB.
- Easily deployable (Render, Koyeb, VPS, etc).

---

## 🌐 Environment Variables

You need to set the following variables (e.g., in `.env` or Render/Koyeb config):

```env
API_ID=your_api_id
API_HASH=your_api_hash
SESSION=your_bot_token
ADMINS=your_telegram_id_or_username
DB_URL=your_mongodb_connection_uri


---

⚙️ Installation

git clone https://github.com/the-lx0980/CNL-Auto-Post-Bot.git
cd CNL-Auto-Post-Bot

# Setup virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt


---

▶️ Run the Bot

python main.py


---

📚 Commands

> Make sure the bot is admin in both source and target channels.



Command	Description

/add sourceID targetID	Add a new forward mapping
/list	List all current mappings
/remove sourceID	Remove a specific source mapping
/start	Check if the bot is alive



---

🧪 Example

/add -1001234567890 -1009876543210

This will forward posts from channel -1001234567890 to -1009876543210.


---

🚀 Deployment Tips

You can deploy it for free using:

Render

Koyeb

Heroku (via worker dyno)

Railway.app


Make sure to use python main.py as the start command.


---

📜 License

MIT License
Maintained by @the-lx0980

---

Let me know if you want a version in **Hindi**, or instructions for **Render/Koyeb-specific deployment**.

