from dogehouse import DogeClient, event, command
from dogehouse.entities import User, Message, UserPreview
import os

from random import choice, randint

import asyncio

import requests

from dotenv import load_dotenv

from typing import Optional, Union

from owoify import Owoifator
owoifator = Owoifator()

load_dotenv()

import json

with open("config.json") as config_file:
    config = json.load(config_file)

VERSION = "1.0.3"

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

    # TODO: Implement `on_user_leave`

    # @Arthurdw 
    @event
    async def on_speaker_request(self, user: str, _):
        user: Union[User, UserPreview] = [usr for usr in self.room.users if usr.id == user][0]
        await self.send(f"🎤 Welcome to the stage - {user.mention if isinstance(user, User) else user.displayname}")
        await self.add_speaker(user)

    # TODO: Fix commands: ["addspeaker", "ban", "unban", "banchat"]

    # @command(name="addspeaker")
    # async def add_speaker_command(self, ctx, user: User):
    #     if ctx.author.username == "mmattbtw":
    #         await self.add_speaker(user)
    #         await self.send(f"🎤 Welcome to the stage - {user.username}")
    #     else:
    #         await self.send("Sorry, you can't use this command.")

    # @command(name="ban")
    # async def ban_command(self, ctx, user: User):
    #     if ctx.author.username == "mmattbtw":
    #         await self.ban(user.id)
    #         await self.send("🔨 User has been banned.")
    #     else:
    #         await self.send("Sorry, you can't use this command.")

    # @command(name="unban")
    # async def unban_command(self, ctx, user: User):
    #     if ctx.author.username == "mmattbtw":
    #         await self.unban(user.id)
    #         await self.send(f"💖 {user.username} has been unbanned.")
    #     else:
    #         await self.send("Sorry, you can't use this command.")

    # @command(name="banchat")
    # async def ban_chat_command(self, ctx, user: User):
    #     if ctx.author.username == "mmattbtw":
    #         await self.ban_chat(user)
    #         await self.send("🔨 User has been chat banned.")
    #     else:
    #         await self.send("Sorry, you can't use this command.")

    @command(name="userid")
    async def get_userid_command(self, ctx):
        await self.send(f"Your user ID is: {ctx.author.id}")

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

    @command(name="owoify")
    async def owoify_command(self, ctx, Message, *, message):
        owo_text = owoifator.owoify(text=message)

        await self.send(f"{owo_text}")

    async def valroll_func(self, ctx):
        characters = (
            "Viper",
            "Sova",
            "Sage",
            "Reyna",
            "Raze",
            "Phoenix",
            "Omen",
            "Jett",
            "Cypher",
            "Brimstone",
            "Breach",
            "Killjoy",
            "Skye",
            "Yoru",
            "Astra",
        )

        char = choice((characters))

        await self.send(f"I think you should play {char}.  :peepoHappy:")

    @command(name="valroll")
    async def valroll_command(self, ctx):
        await self.valroll_func(ctx)


if __name__ == "__main__":
    Client(
        os.environ.get("TOKEN"),
        os.environ.get("REFRESH_TOKEN"),
        prefix=config["prefix"],
    ).run()
