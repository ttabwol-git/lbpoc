import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackWebClient:

    def __init__(self) -> None:
        self.client = WebClient(token=os.environ['SLACK_API_TOKEN'])
        self.bot_name = os.environ['SLACK_BOT_NAME']

    def send_message(self, channel: str, message: str) -> dict:
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=message,
                username=self.bot_name,
                icon_emoji=":robot_face:"
            )
            return response.data
        except SlackApiError as e:
            return e.response.data

