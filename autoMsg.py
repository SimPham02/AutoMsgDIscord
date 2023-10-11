import time
import requests
import random

tokens = [""]
channelid = ""

def msg(msg):
    for token in tokens:
        payload = {"content": msg}
        header = {"authorization": token}
        response = requests.get("https://discord.com/api/users/@me", headers=header)

        if response.status_code == 200:
            data = response.json()
            account_name = f"{data['username']}#{data['discriminator']}"
        else:
            account_name = "**You have not set tokens properly**"
        url = f"https://discord.com/api/v9/channels/{channelid}/messages"
        r = requests.post(url, data=payload, headers=header)
        if r.status_code == 200:
            print(f"Sent {msg} successfully in id {account_name}")
        else:
            print(f"Error in sending {msg} in user {account_name}")

if __name__ == "__main__":
    messages = ["Message 1",
                "Message 2", 
                "Message 3", 
                "Message 4", 
                "Message 5"]
    while True:
        time.sleep(random.randrange(1, 5))
        selected_message = random.choice(messages)
        msg(selected_message)
