import subprocess
import os
from os.path import join
from texttospeech import tts


# This function contains commands that can be called from the instruction_listener function.
def commands(instruction):
    if "open Spotify" in instruction:
        tts("Opening Spotify")
        spotify = "Spotify.exe"
        for root, dirs, files in os.walk("C:\\"):
            if spotify in files:
                print("Found Spotify in " + join(root, spotify))
                break
            else:
                print("searching...")
        command = join(root, spotify)
        subprocess.Popen(command)
        return

    if "open Google Chrome" in instruction:
        tts("Opening Google Chrome")
        chrome = "chrome.exe"
        for root, dirs, files in os.walk("C:\\"):
            # print("searching", root)
            if chrome in files:
                print("found " + join(root, chrome))
                break
        command = join(root, chrome)
        subprocess.Popen(command)
        return
    '''
    if "open Google Chrome" in instruction:
        command = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(command)
    '''
    if "nothing" in instruction:
        tts("Okay")
        return

    else:
        return "failure"

