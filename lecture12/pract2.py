from flask import Flask,request
import requests,json
app = Flask("chatbot")
token = "12345678910"
def bot(recipient,text):
    url = r"https://graph.facebook.com/v6.0/me/messages?access_token=EAAIqcGvJoV0BAEAZCC2MolaQgZAn8vJnZCsUCWl6uYlYQPvlBQZCJi7CDQPVvIt9LoMgZAGxWXPQA9ELtrsm5apACpzLTQvkFLa5ofscHb0IyPZALoJ8KIbbgO9v3I0FSj1aW3I5OqKAyvZC0Em5fdYxEGgitgUuKCZBHtfq2CjQGDMFZBVffaPxUqsZCtLIRSl3EZD"
    if text in ["hi","Hi","HI","hello","Good morning","Good Afternoon","Good evening","Good night","HELLO","Hello","HEY","hey","Hey"]:
        d1 ={
            "recipient":
                {
                    "id":recipient
                },
            "message":
                {
                    "text" : text + " client"
                }
        }
        requests.post(url,json=d1)
    elif text in ["Pandas","PANDAS","SEND PANDAS","pandas","send pandas photos","send Pandas Photos","Send Pandas Photo"]:
        d1 = {
            "recipient": {
                "id": recipient
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": r"https://c402277.ssl.cf1.rackcdn.com/photos/18315/images/hero_small/Medium_WW230176.jpg?1576168323",
                        "is_reusable": True
                    }
                }
            }
        }
        requests.post(url, json=d1)
    elif text in ["Shabaz","Shabaz","SEND Shabaz","Shabaz","send Shabaz photos","send Shabaz Photos","Send Shabaz Photo"]:
        d1 = {
            "recipient": {
                "id": recipient
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": r"https://scontent.fdel11-1.fna.fbcdn.net/v/t1.0-9/s960x960/81625923_480212512907634_2164245260383813632_o.jpg?_nc_cat=106&_nc_ohc=ShwvU39HKO4AX9AgP-H&_nc_ht=scontent.fdel11-1.fna&oh=58fedeab0e346af68bda7b65e0d58c40&oe=5EBD03FD",
                        "is_reusable": True
                    }
                }
            }
        }
        requests.post(url, json=d1)
    elif text in ["Adnan","Adnan","SEND Adnan","Adnan","send Adnan photos","send Adnan Photos","Send Adnan Photo"]:
        d1 = {
            "recipient": {
                "id": recipient
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": r"https://scontent.fdel11-1.fna.fbcdn.net/v/t1.0-9/12933071_1694890100771077_292427234595329218_n.jpg?_nc_cat=102&_nc_ohc=pFRXrkpWlQoAX_fPciB&_nc_ht=scontent.fdel11-1.fna&oh=8f2a221bd4fa22fd3d8154e7b0d89f33&oe=5EBE6420",
                        "is_reusable": True
                    }
                }
            }
        }
        requests.post(url, json=d1)
    elif text in ["Zahid","Zahid","SEND Zahid","Zahid","send Zahid photos","send Zahid Photos","Send Zahid Photo"]:
        d1 = {
            "recipient": {
                "id": recipient
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": r"https://scontent.fdel11-1.fna.fbcdn.net/v/t31.0-8/s960x960/10620218_1542283732656181_1122426862339360895_o.jpg?_nc_cat=106&_nc_ohc=kr05tXFkW74AX8Unyu5&_nc_ht=scontent.fdel11-1.fna&oh=6692c9f05b44350bf4c591a9df500e1e&oe=5EBCD027",
                        "is_reusable": True
                    }
                }
            }
        }
        requests.post(url, json=d1)
    elif text in ["Osaid","Osaid","SEND Osaid","Osaid","send Osaid photos","send Osaid Photos","Send Osaid Photo"]:
        d1 = {
            "recipient": {
                "id": recipient
            },
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": r"https://scontent.fdel11-1.fna.fbcdn.net/v/t1.0-9/10599228_275617392625580_6872905880470087064_n.jpg?_nc_cat=108&_nc_ohc=6lS8-rEjWGEAX_StAbR&_nc_ht=scontent.fdel11-1.fna&oh=c1b2eb69ed9a2970ff615456e17dcf10&oe=5EBDA39B",
                        "is_reusable": True
                    }
                }
            }
        }
        requests.post(url, json=d1)
    elif text in ["call"]:
        d1 = {
            "recipient":
                {
                    "id": recipient
                },
            "message":
                {
                    "attachment":
                        {
                            "type":"template",
                            "payload":
                                {
                                    "template_type":"button",
                                    "text":"Need Further assistance",
                                    "buttons":[{"type":"phone_number","title":"msg","payload":"+918851670802"}]
                                }
                        }
                }
        }
        requests.post(url,json=d1)
    else:
        d1 = {
            "recipient":
                {
                    "id": recipient
                },
            "message":
                {
                    "text": "bot says " + text
                }
        }
        requests.post(url, json=d1)

@app.route("/check/")
def check():
    return "working"

@app.route("/callback/",methods=["GET"])
def get_callback():
    if token == request.args.get("hub.verify_token"):
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
                text="bot has nothin to say"
                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")
                print(sender,recipient,text)
                bot(sender,text)

    return "done"

app.run()