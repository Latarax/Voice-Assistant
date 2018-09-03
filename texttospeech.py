import pyttsx3

# This function enables text to speech.
# It takes the speech that was converted into text as input from the instruction_listener function
# and outputs a spoken response.


def tts(text):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate-50)
    engine.say(text)
    engine.runAndWait()
