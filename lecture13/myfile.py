from flask import Flask, request
from pymessenger.bot import Bot
import requests, json

app = Flask("hello")

VERIFY_TOKEN = "1234567890"
ACCESS_TOKEN = "EAAIqcGvJoV0BALb3FGMNGRIfkUk3Fb16wZCfPKZBjp0NZCXQZCEA7iAGoYmSZBZAvZBq6hWf2LmqIgDtVXQS9wet22axo47L8LZArFeHBwwKA8tox7F3LhMTOyt2ZAZAIcD5nmLnOdTlveQZACq5t3cNsKd6JZCkOMA2S3jqEEiTvXgAAjGK7XFP7bL93vm0wn0yDXkZD"

pybot = Bot(ACCESS_TOKEN)

@app.route("/check/", methods=["GET"])
def sayhi():
    return "working"


@app.route("/callback/", methods=["GET"])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "not working"


@app.route("/callback/", methods=["POST"])
def post_callback():
    output = request.get_json()

    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")
                text = "You sent an attachment"
                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")

                print(sender, recipient, text)
                pybot.send_text_message(sender, text)
                pybot.send_image_url(sender,r"https://d1hlpam123zqko.cloudfront.net/383/588/791/910003003-1s867he-gipb0mqaeqri08a/original/RecentlyUpdated.jpg")
    return "done"


app.run()
