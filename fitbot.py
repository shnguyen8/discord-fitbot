import discord
import random
from dotenv import load_dotenv
import os

load_dotenv()

# create an object with different exercises
exercises = [
    {"name": "deadlift", "type": "pull"},
    {"name": "pull-ups", "type": "pull"},
    {"name": "bent-over rows", "type": "pull"},
    {"name": "lat pulldowns", "type": "pull"},
    {"name": "seated cable rows", "type": "pull"},
    {"name": "bicep curls", "type": "pull"},
    {"name": "bench press", "type": "push"},
    {"name": "overhead shoulder press", "type": "push"},
    {"name": "incline dumbbell press", "type": "push"},
    {"name": "tricep dips", "type": "push"},
    {"name": "push-ups", "type": "push"},
    {"name": "lateral raises", "type": "push"},
    {"name": "squats", "type": "leg"},
    {"name": "lunges", "type": "leg"},
    {"name": "bulgarian split squats", "type": "leg"},
    {"name": "leg press", "type": "leg"},
    {"name": "calf raises", "type": "leg"},
    {"name": "romanian deadlifts", "type": "leg"},
    {"name": "30 minutes of running", "type": "cardio"},
    {"name": "45 minutes of cycling", "type": "cardio"},
    {"name": "15 minutes of rowing", "type": "cardio"},
    {"name": "20 minutes of jump roping", "type": "cardio"},
    {"name": "20 minutes of stair climbing", "type": "cardio"},
    {"name": "30 minutes of incline walking", "type": "cardio"},
]

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    pull_list = []
    push_list = []
    leg_list = []
    cardio_list = []
    for exercise in exercises:
        if exercise["type"] == "pull":
            pull_list.append(exercise["name"])

        if exercise["type"] == "push":
            push_list.append(exercise["name"])

        if exercise["type"] == "leg":
            leg_list.append(exercise["name"])

        if exercise["type"] == "cardio":
            cardio_list.append(exercise["name"])

    if message.author == client.user:
        return
    # prompt user to ask for a push day, pull day, leg day, or cardio day
    if message.content.startswith("/hello"):
        await message.channel.send(
            "Hello! Type in /pull, /push, /leg, or /cardio for a randomized workout set."
        )
    # present user with 3 randomly generated exercises depending on the day that was requested
    if message.content.startswith("/pull"):
        if len(pull_list) >= 3:
            pull_day = random.sample(pull_list, 3)
            await message.channel.send(
                "Try this set of exercises for your ***pull-day***: "
                + ", ".join(pull_day)
            )

    if message.content.startswith("/push"):
        if len(push_list) >= 3:
            push_day = random.sample(push_list, 3)
            await message.channel.send(
                "Try this set of exercises for your ***push-day***: "
                + ", ".join(push_day)
            )

    if message.content.startswith("/leg"):
        if len(leg_list) >= 3:
            leg_day = random.sample(leg_list, 3)
            await message.channel.send(
                "Try this set of exercises for your ***leg-day***: "
                + ", ".join(leg_day)
            )

    if message.content.startswith("/cardio"):
        if len(cardio_list) >= 3:
            cardio_day = random.sample(cardio_list, 2)
            await message.channel.send(
                "Try this set of exercises for your ***cardio-day***: "
                + ", ".join(cardio_day)
            )


client.run(BOT_TOKEN)
