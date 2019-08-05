import os
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

client = Client(
    os.environ.get('TWILIO_ACCOUNT_SID'),
    os.environ.get('TWILIO_AUTH_TOKEN')
)


@app.route('/send-sms/')
def send_sms():
    msg = client.messages.create(
        body="This is the message content @omiguelperez.",
        from_=os.environ.get('TWILIO_FROM'),
        to=os.environ.get('TWILIO_TO')
    )
    return msg.sid
