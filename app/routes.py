from flask import Blueprint, jsonify, request

from .ai_responder import get_ai_response
from .config import Config
from .faq_responder import get_faq_response
from .messenger import send_text_message

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def index():
    return "Hello world, I am a Python chat bot"


@bp.route("/webhook/", methods=["GET", "POST"])
def webhook():
    print("\n=== New Request ===")  # Debug log
    print(f"Request method: {request.method}")  # Debug log
    print(f"Request args: {request.args}")  # Debug log

    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        print(f"Verify token from request: {verify_token}")  # Debug log
        print(f"Expected verify token: {Config.FB_VERIFY_TOKEN}")  # Debug log

        if verify_token == Config.FB_VERIFY_TOKEN:
            print("Token matches! Returning challenge.")  # Debug log
            return challenge, 200
        else:
            print("Token does not match!")  # Debug log
            return "Error, wrong token", 403

    elif request.method == "POST":
        print("POST data:", request.data)  # <--- Add this line
        data = request.get_json()
        print("Parsed JSON:", data)  # <--- Add this line
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event["sender"]["id"]
                if "message" in event and "text" in event["message"]:
                    text = event["message"]["text"]
                    response = get_faq_response(text)
                    if response:
                        send_text_message(sender_id, response)
                    else:
                        send_text_message(sender_id, get_ai_response(text))
                elif "postback" in event:
                    send_text_message(
                        sender_id, f"Postback received: {event['postback']}"
                    )
        return "ok", 200
