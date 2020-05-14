# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
#information kept locally for security
account_sid = 'hidden'
auth_token = 'hidden'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hellloooo",
                     from_='hidden', #number obtained from twilio, kept hidden for security
                     to='+13303109608'
                 )

print(message.sid)
