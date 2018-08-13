import speech_recognition as sr
import winsound
import subprocess
import webbrowser


# This program listens for the trigger word "hello there" and listens for commands.

# This function listens for the trigger word "hello there" and goes to the instruction_listener function.
# It loops back if the trigger word is not heard.
def trigger_listener():
    x = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say hello there to trigger instructions.")
        audio = x.listen(source)
        try:
            trigger = x.recognize_google(audio)
            if "hello there" in trigger:
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
            winsound.PlaySound("swvader03", winsound.SND_FILENAME)
            print("You said: " + instruction)
            commands(instruction)
        except sr.UnknownValueError:
            print("Try again")
            instruction = instruction_listener()
            return instruction


# This function contains commands that can be called from the instruction_listener function.
def commands(instruction):

    if "open Spotify" in instruction:
        command = "Spotify"
        subprocess.Popen(command)
        print("Yes, my master")

    if "open Google Chrome" in instruction:
        command = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(command)
        print("Yes, my master")

    if "nothing" in instruction:
        print("Yes my master.")


# Infinite loop for program
while True:
    trigger_listener()
