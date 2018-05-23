#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
from translate import Translator
import speech_recognition as sr
from gtts import gTTS
import time
import threading
import os
import _thread
from pygame import mixer
from stopit import async_raise, TimeoutException
from stopit import ThreadingTimeout as Timeout, threading_timeoutable as timeoutable
#import keyboard
# obtain audio from the microphone


def translate_for_me(fromLang, toLang, text):
    secret = '75a648040ae949f594acc7b25221a622'
    translator = Translator(provider='microsoft', from_lang=fromLang,
                            to_lang=toLang, secret_access_key=secret)
    translation = translator.translate(text)
    return translation


def play(text):
    mixer.init()
    mixer.music.load(text)
    mixer.music.play()
    while(mixer.music.get_busy()):
        pass


def delete(text):
    time.sleep(1)
    mixer.music.load("Holder.mp3")
    # os.remove(text)


def test(self):
    print("hello olo")
    return "สวัสดีครับผม"


def listen(language):
    if language == 'th':
        to_lang = 'en'
    else:
        to_lang = 'th'
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
        with Timeout(10, swallow_exc=False) as timeout_ctx:
            print("listen finished sending to google")
            if language == 'th':
                text = r.recognize_google(audio, language="th-TH")
            else:
                text = r.recognize_google(audio, language="en-US")
        # play("end.mp3")
        # delete("end.mp3")
        print(time.time()-start)
        print("convert to text done")
        print("Google Speech Recognition thinks you said " +
              text)
        result = translate_for_me(language, to_lang, text)
        tts = gTTS(result, lang=to_lang, slow=False)
        tts.save('testtrans.mp3')
        play('testtrans.mp3')
        delete('testtrans.mp3')
        return text+','+result
    except TimeoutException:
        print("too slow")
        return "too slow"
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "error1239123"
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.WaitTimeoutError:
        print("waiting too long")
    except:
        try:
            with Timeout(10, swallow_exc=False) as timeout_ctx:
                if language == 'th':
                    text = r.recognize_google(audio, language="th-TH")
                else:
                    text = r.recognize_google(audio, language="en-US")
            # play("end.mp3")
            # delete("end.mp3")
            print(time.time()-start)
            print("convert to text done")
            # tts = gTTS(text, lang='th', slow=False)

            print("Google Speech Recognition thinks you said " +
                  text)
            result = translate_for_me(language, to_lang, text)
            tts = gTTS(result, lang=to_lang, slow=False)
            tts.save('testtrans.mp3')
            play('testtrans.mp3')
            time.sleep(5)
            delete('testtrans.mp3')
            return text+','+result
        except TimeoutException:
            print("too slow")
            return "too slow"


# print(translate_for_me('th', 'en', 'สวัสดี'))
# print(listen('th'))
