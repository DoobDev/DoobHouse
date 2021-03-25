from dogehouse import DogeClient, event, command
from dogehouse.entities import User, Message
import os

from dotenv import load_dotenv

load_dotenv()

import json

with open("config.json") as config_file:
    config = json.load(config_file)

class Client(DogeClient):
    @event
    async def on_ready(self):
        print(f"Successfully connected as {self.user}!")
        await self.join_room(config["room"])
        
    @command(name="ping")
    async def ping_command(self, ctx):
        await self.send("pong")
            

if __name__ == "__main__":
    Client(os.environ.get("TOKEN"), os.environ.get("REFRESH_TOKEN"), prefix=".").run()