# Pushover tools: 

import http.client, urllib
import requests


class pushover:
    def __init__(self):

        self.sender= 'Sender name'
        self.app_token_message = 'your app token'
        self.user_key_pushover = 'your pushover user key'
        
    def send_message(self,message,title,*args):


        if len(args)>0:
            sound=args[0]
        else:
            sound = "pushover"   # Default sound 

        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": self.app_token_message,
            "user": self.user_key_pushover,
            "message": message,
            "title": title,
            "sound": sound
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()

    def send_image(self, message, title, path_to_file):
        r = requests.post("https://api.pushover.net/1/messages.json",
                        data = {"token" : self.app_token_message,
                        "user" : self.user_key_pushover,
                        "message" : message,
                        "title" : title},
                        files={"attachment":open(path_to_file,"rb")})





