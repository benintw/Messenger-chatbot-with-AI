import requests

from .config import Config


def send_text_message(recipient_id: str, text: str) -> None:
    """Send a text message using Facebook Messenger Send API."""
    payload = {"recipient": {"id": recipient_id}, "message": {"text": text}}
    params = {"access_token": Config.FB_PAGE_ACCESS_TOKEN}
    response = requests.post(
        "https://graph.facebook.com/v2.6/me/messages", params=params, json=payload
    )
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
