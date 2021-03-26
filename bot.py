from dogehouse import DogeClient, event, command
from dogehouse.entities import User, Message
import os

import asyncio

import requests

from dotenv import load_dotenv

load_dotenv()

import json

with open("config.json") as config_file:
    config = json.load(config_file)

VERSION = "1.0.2"

class Client(DogeClient):
    @event
    async def on_ready(self):
        print(f"Successfully connected as {self.user}!")
        #await self.join_room(config["room"])
        await self.create_room(name="DoobHouse! [[TESTING]]", description="GitHub.com/DoobDev/DoobHouse (or d!repo)\nType d!letmespeak to get up on the stage.\nType d!help for the commands!")
        await asyncio.sleep(2)
        await self.send(f"Doob is online! (Running version {VERSION})")

    @event
    async def on_message(self, message: Message):
        print(f"[MESSAGE LOGS] {message.author} - {message.content}")

    @event
    async def on_user_join(self, user: User):
        await self.send(f"👋 Welcome to the room - {user.username}")

    @event
    async def on_speaker_request(self, user: User):
        await self.send(f"🎤 Welcome to the stage - {user.username}")
        await self.add_speaker(user)

    @command(name="letmespeak")
    async def speak_command(self, ctx):
        await self.send(f"🎤 Welcome to the stage - {ctx.author.username}")
        await self.add_speaker(ctx.author)

    @command(name="ping")
    async def ping_command(self, ctx):
        await self.send(f"🏓 Pong!~")

    @command(name="help")
    async def help_command(self, ctx):
        await self.send(
            "You can find all of the commands over at: https://docs.doobbot.com/doobhouse-commands"
        )

    @command(name="dogfact")
    async def dogfact_command(self, ctx):
        URL = "https://some-random-api.ml/facts/dog"

        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            await self.send("Here is a dog fact! - " + data["fact"] + "  :DANKIES:")

        else:
            await self.send(
                f"⚠ The Dog Fact api sent out a {response.status_code} code :/"
            )

    @command(name="dogpic")
    async def dogpic_command(self, ctx):
        URL = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(URL)

        if response.status_code == 200:

            data = response.json()

            await self.send(
                "Here is a Dog Pic! - " + data["message"] + "  :peepoHappy:"
            )

        else:
            await self.send(
                f"⚠ The Dog Picture api sent out a {response.status_code} code :/"
            )

    @command(name="dev")
    async def developer_command(self, ctx):
        await self.send(
            ":DANKHACKERMANS: My developer is named mmatt or Matt! You can follow him on GitHub at ==> https://github.com/mmattbtw  :peepoCheer: ~ :DogeHouse: His DogeHouse account is https://dogehouse.tv/user/mmattbtw  :WICKED:"
        )

    @command(name="repo")
    async def repo_command(self, ctx):
        await self.send(
            ":GitHub: This bot is open source on GitHub! https://github.com/doobdev/doobhouse   :DANKHACKERMANS:"
        )

    @command(name="asktospeak")
    async def ask_to_speak_command(self, ctx):
        if ctx.author.username == "mmattbtw":
            await self.send("Can I speak...?  :peepoHug:")
            await self.ask_to_speak()
        else:
            await self.send("⚠ Sorry, you can't ask to speak!")

    @command(name="dogehouse")
    async def dogehouse_command(self, ctx):
        response = requests.get(url="https://api.dogehouse.xyz/v1/statistics")
        data = response.json()

        totalRooms = str(data["totalRooms"])
        totalScheduledRooms = str(data["totalScheduledRooms"])
        totalOnline = str(data["totalOnline"])

        if response.status_code == 200:
            await self.send(
                "DogeHouse Stats :DogeHouse:   Total Rooms - "
                + totalRooms
                + ", Total Scheduled Rooms - "
                + totalScheduledRooms
                + ", Total Online - "
                + totalOnline
            )

        else:
            await self.send(
                f"⚠ The DogeHouse API responded with a `{response.status_code}` status code."
            )


if __name__ == "__main__":
    Client(
        os.environ.get("TOKEN"),
        os.environ.get("REFRESH_TOKEN"),
        prefix=config["prefix"],
    ).run()
