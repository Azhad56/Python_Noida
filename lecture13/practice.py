from flask import Flask,request
import requests,json
from pymessenger.bot import Bot
app = Flask("chatbot")
VERIFY_TOKEN = "12345678910"
ACCESS_TOKEN ="EAAIqcGvJoV0BAEAZCC2MolaQgZAn8vJnZCsUCWl6uYlYQPvlBQZCJi7CDQPVvIt9LoMgZAGxWXPQA9ELtrsm5apACpzLTQvkFLa5ofscHb0IyPZALoJ8KIbbgO9v3I0FSj1aW3I5OqKAyvZC0Em5fdYxEGgitgUuKCZBHtfq2CjQGDMFZBVffaPxUqsZCtLIRSl3EZD"
pybot = Bot(ACCESS_TOKEN)
@app.route("/check/")
def check():
    return "working"

@app.route("/callback/",methods=["GET"])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "Not Working"
@app.route("/callback/",methods=["POST"])
def post_callback():
    output = request.get_json()
    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")
                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")
                print(sender,recipient,text)
                pybot.send_text_message(sender,"bot says "+text)

    return "done"

app.run()