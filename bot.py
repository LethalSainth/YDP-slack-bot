import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


load_dotenv() 
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']


client = WebClient(token=SLACK_BOT_TOKEN)

try: 
    response = client.chat_postMessage(channel='#random', text="Sneaked into this bitch today lol :robot_face:")
    

    # client.conversations_leave(channel='C037A9Z7FGS')

except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")