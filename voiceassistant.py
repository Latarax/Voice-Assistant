# This program listens for the trigger word "computer" and listens for commands.

import speech_recognition as sr
import winsound
import wolframalpha
from commands import commands
from texttospeech import tts


def wolfram(question):
    app_id = "5AXQ5J-3W6A7YU5Q9"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    return answer


# This function listens for the trigger word "computer" and goes to the instruction_listener function.
# It loops back if the trigger word is not heard.
def trigger_listener():
    print("Say \"computer\" to trigger voice assistant.")
    x = sr.Recognizer()
    with sr.Microphone() as source:
        audio = x.listen(source)
        try:
            trigger = x.recognize_google(audio)
            if "computer" in trigger:
                instruction_listener()
        except sr.UnknownValueError:
            trigger = trigger_listener()
            return trigger


# This function listens for commands written in the john function and goes to that function.
# It loops back if the trigger word is not heard.
def instruction_listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What is thy bidding, my master?")
        winsound.PlaySound("swvader04", winsound.SND_FILENAME)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            instruction = r.recognize_google(audio)
            # winsound.PlaySound("swvader03", winsound.SND_FILENAME)
            print(instruction)
            done = commands(instruction)
            if done == "failure":
                answer = wolfram(instruction)
                print(answer)
                tts(answer)
        except sr.UnknownValueError:
            print("Try again")
            instruction = instruction_listener()
            return instruction


# Infinite loop for program
def loop(event):
    while True:
        trigger_listener()
