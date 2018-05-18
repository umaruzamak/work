#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os
#import keyboard
# obtain audio from the microphone


class Test_Drive:
    def test():
        print("hello olo")
        return "สวัสดีครับผม"

    def listen():
        playsound("start.mp3")
        r = sr.Recognizer()
        print("Say something!")
        start = time.time()
        with sr.Microphone() as source:
            print(time.time()-start)
            audio = r.listen(source)
            print(time.time()-start)

        try:
            soundfile = "temp.mp3"
            try:
                time.sleep(2)
                os.remove(soundfile)
            except:
                pass
            print(time.time()-start)
            print("listen")
            playsound("end.mp3")
            text = r.recognize_google(audio, language="th-TH")
            print(time.time()-start)
            print("get it")
            tts = gTTS(text, lang='th', slow=False)
            try:
                time.sleep(2)
                tts.save(soundfile)
            except:
                try:
                    time.sleep(2)
                    tts.save(soundfile)
                except:
                    pass
            print("Google Speech Recognition thinks you said " +
                  r.recognize_google(audio, language="th-TH"))
            playsound(soundfile)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.WaitTimeoutError:
            print("waiting too long")

    def listenEN():
        playsound("start.mp3")
        r = sr.Recognizer()
        print("Say something!")
        start = time.time()
        with sr.Microphone() as source:
            print(time.time()-start)
            audio = r.listen(source)
            print(time.time()-start)

        try:
            soundfile = "temp.mp3"
            try:
                time.sleep(2)
                os.remove(soundfile)
            except:
                pass
            print(time.time()-start)
            print("listen")
            playsound("end.mp3")
            text = r.recognize_google(audio, language="en-US")
            print(time.time()-start)
            print("get it")
            tts = gTTS(text, lang='en', slow=False)
            try:
                time.sleep(2)
                tts.save(soundfile)
            except:
                try:
                    time.sleep(2)
                    tts.save(soundfile)
                except:
                    pass
            print("Google Speech Recognition thinks you said " +
                  r.recognize_google(audio, language="th-TH"))
            playsound(soundfile)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.WaitTimeoutError:
            print("waiting too long")


# print(Test_Drive.listen())
