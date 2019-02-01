# All the important ID stuff
from credentials import (account_sid, auth_token, my_twilio_whatsapp, my_cell, my_twilio, giphy_api_key)

import schedule
import requests
import giphy_client

from twilio.rest import (Client, TwilioRestClient)
from twilio.base.exceptions import TwilioRestException
from twilio.twiml.messaging_response import MessagingResponse

from giphy_client.rest import ApiException
from pprint import pprint

from flask import Flask

app = Flask(__name__)

# Twilio - creating a new record
client = Client(account_sid, auth_token)

# Twilio - get exisiting record
#existing_client = TwilioRestClient(account_sid, auth_token)

# Giphy
api_instance = giphy_client.DefaultApi()
giphy_api_key = giphy_api_key

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming msgs with friendly SMS"""
    # start response
    resp = MessagingResponse()

    # add message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


#################################################################################
# FUNCTIONS

def get_giphy():
    """Get a random gif"""
    
    tag = "dang"
    fmt = 'json'
    request_url = "https://api.giphy.com/v1/gifs/random?api_key=" + giphy_api_key + "&tag=" + tag + "&fmt=" + fmt
    payload = '{}'

    try:
        # api_response = api_instance.gifs_random_get(giphy_api_key, tag=tag, fmt=fmt)
        # pprint(api_response)
        gif = requests.request("GET", request_url, data=payload).json()
        return gif['data']['images']['fixed_height_small']['mp4'], tag

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)

def send_MMS():
    """Sends to cell"""
    media, body = get_giphy()
    try:
        message = client.messages.create(
            body=body,
            media_url=media,
            to=my_cell,    # Replace with your phone number
            from_=my_twilio) # Replace with your Twilio number
        print("Message sent!")
    # If an error occurs, print it out.
    except TwilioRestException as e:
        print(e)

schedule.every(5).seconds.do(send_MMS)

while True:
    schedule.run_pending()

################################################################################

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True) 
