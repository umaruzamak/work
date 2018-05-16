#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import datetime
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    sstart = datetime.datetime.now()
    text = r.recognize_google(audio,language = "th-TH")
    print(str(datetime.datetime.now() - sstart))
    
    tts = gTTS(text,lang='th',slow=True)
    tts.save("temp.mp3")
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language = "th-TH"))
    playsound("temp.mp3")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
print("GG")
print("GG")
# recognize speech using Google Cloud Speech
# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
# try:
#     print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# except sr.UnknownValueError:
#     print("Google Cloud Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Cloud Speech service; {0}".format(e))

