**Simple Telegram Bot - Questioning and Chat Initiation**

This project is a simple Telegram bot that presents a question in a chatroom and grants users the ability to start chatting after answering the question correctly.

**Installation and Execution**

1. Install the `python-telegram-bot` library.
```bash
pip install python-telegram-bot
```

2. Download the source code and provide your Telegram bot token.
```python
# Please enter your Telegram bot token.
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

3. Run the code.
```bash
python your_bot_script.py
```

**Functionality**

1. When the bot joins a chatroom, it randomly presents a question to the users.
2. Upon answering the question correctly, users will see a button to initiate chatting.
3. Users can click the button to begin chatting and engage with all participants freely.

**User Guide**

1. Add the bot to your Telegram chatroom.
2. Once the bot joins the chatroom, it will randomly present a question.
3. Users can respond with their answer via chat.
4. If the answer is correct, a "Start Chatting" button will appear.
5. Click the "Start Chatting" button to initiate chatting.

**Note**

- While the bot is presenting a question, other users' chat messages will not be visible.
- In case of an incorrect answer, the bot will present a new question.

**License**

This project is licensed under the MIT License. For more details, please see the LICENSE file.
