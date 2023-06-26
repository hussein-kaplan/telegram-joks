import telebot
import requests
import time

# Set your Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Create a telebot instance
bot = telebot.TeleBot(TOKEN)

# Set your channel ID
channel_id = '@YOUR_CHANNEL_USERNAME'

# API endpoint for fetching jokes
joke_api_url = 'https://v2.jokeapi.dev/joke/Any'

# Function to fetch a joke from the API
def get_joke():
    response = requests.get(joke_api_url)
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data['type'] == 'single':
            return joke_data['joke']
        elif joke_data['type'] == 'twopart':
            return f"{joke_data['setup']}\n{joke_data['delivery']}"
    return None

# Function to publish the joke in the channel
def publish_joke():
    joke = get_joke()
    if joke:
        bot.send_message(chat_id=channel_id, text=joke)
    else:
        bot.send_message(chat_id=channel_id, text="Unable to fetch joke.")

# Call the publish_joke function every hour
while True:
    publish_joke()
    time.sleep(3600)  # Delay for an hour (3600 seconds)

# Start the bot
bot.polling()
