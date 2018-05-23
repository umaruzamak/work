#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import threading
import os
from pygame import mixer
from stopit import async_raise, TimeoutException
# doctest: +SKIP
from stopit import ThreadingTimeout as Timeout, threading_timeoutable as timeoutable
#import keyboard
# obtain audio from the microphone


def play(text):
    mixer.init()
    mixer.music.load(text)
    mixer.music.play()


def delete(text):
    time.sleep(2)
    mixer.music.load("Holder.mp3")
    # os.remove(text)
# def startloop():
#     mythread = threading.Thread(target=self.listen)
#     mythread.start()
#     thistime = time.time()
#     while thistime + 20 > time.time(): # 5 seconds
#         time.sleep(1)


def listen():

    try:
        with Timeout(30.0, swallow_exc=False) as timeout_ctx:
            # play("start.mp3")
            # delete("start.mp3")
            r = sr.Recognizer()
            print("Say something!")
            start = time.time()
            with sr.Microphone() as source:
                print(time.time()-start)
                audio = r.listen(source)
                print(time.time()-start)

            try:
                soundfile = "temp.mp3"
                print(time.time()-start)
                print("listen")
                # play("end.mp3")
                # delete("end.mp3")
                text = r.recognize_google(audio, language="th-TH")
                print(time.time()-start)
                print("get it")
                # tts = gTTS(text, lang='th', slow=False)

                print("Google Speech Recognition thinks you said " +
                      text)
                # playsound(soundfile)
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                return "error1239123"
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(e))
            except sr.WaitTimeoutError:
                print("waiting too long")
    except TimeoutException:
        print("too slow")
        return "too slow"


class Test_Drive:
    def test():
        print("hello olo")
        return "สวัสดีครับผม"

    def listen():
        play("start.mp3")
        delete("start.mp3")
        r = sr.Recognizer()
        print("Say something!")
        start = time.time()
        with sr.Microphone() as source:
            print(time.time()-start)
            audio = r.listen(source)
            print(time.time()-start)

        try:
            soundfile = "temp.mp3"
            print(time.time()-start)
            print("listen")
            # play("end.mp3")
            # delete("end.mp3")
            text = r.recognize_google(audio, language="th-TH")
            print(time.time()-start)
            print("get it")
            # tts = gTTS(text, lang='th', slow=False)

            print("Google Speech Recognition thinks you said " +
                  text)
            # playsound(soundfile)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "error1239123"
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


listen()
# print(Test_Drive.listen())
