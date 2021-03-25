from dogehouse import DogeClient, event, command
from dogehouse.entities import Message

import os

from dotenv import load_dotenv

load_dotenv()


class Client(DogeClient):
    @event
    async def on_ready(self):
        await self.join_room(id="8b4341bb-5ceb-47e2-9bae-00f6db4e20ea")
        print(f"Successfully connected as {self.user}!")

    @command
    async def ping(self, ctx: Message):
        await self.send("pong")


if __name__ == "__main__":
    Client(os.environ.get("TOKEN"), os.environ.get("REFRESH_TOKEN"), prefix="!").run()
