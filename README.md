# twilioapp
An app to try out Twilio's WhatsApp API. 

### REQUIREMENTS 

Requires Python 3.X and Twilio installed.  

**To Install Twilio**

Run `pip install -r requirements.txt`. 

**To Get Twilio Credentials**

1. Go to [www.twilio.com](https://www.twilio.com/try-twilio) to get a free account.
2. Get a free Twilio number.
3. Verify a mobile number (eg., your personal cell or a number that can receive text msgs).
4. Find your `Account SID` and the `Auth Token` on the Twilio console.
 
Also get an API key from [Giphy](https://developers.giphy.com/).

### SETUP

Before running app, be sure to include a `credentials.py` file with your Twilo credentials.

1. Create a python file named `credentials.py`.
2. Add the following to the file:

		account_sid = '[TWILIO ACCT SID]'
		auth_token = '[TWILIO AUTH TOKEN]'
		my_cell = '+[countrycode]YOURMOBILE#'
		my_twilio = '+[countrycode]YOURTWILIO#'
		my_twilio_whatsapp ='+[countrycode]YOURTWILIOWHATSAPP#'
		giphy_api_key = '[GIPHY API KEY]'

