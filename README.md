# Telegram Joke Bot

This is a Telegram bot written in Python that fetches jokes from the Jokeapi.io API and publishes them in a Telegram channel every hour.

## Features

- Fetches random jokes from the Jokeapi.io API.
- Supports both single-line jokes and two-part jokes.
- Publishes the jokes in a specified Telegram channel every hour.
- Provides error handling in case of API failures or inability to fetch jokes.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- telebot library
- requests library

### Installation

1. Clone the repository:

git clone https://github.com/hussein-kaplan/telegram-joks.git



2. Install the required libraries:

pip install telebot requests



### Usage

1. Obtain a Telegram bot token by creating a bot using BotFather.

2. Set your bot token and channel ID in the code:

```python
TOKEN = 'YOUR_BOT_TOKEN'
channel_id = '@YOUR_CHANNEL_USERNAME'
Run the bot script:


The bot will start fetching jokes and publishing them in the specified Telegram channel every hour.

Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
