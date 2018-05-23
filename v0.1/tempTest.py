import sys
import codecs
import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from pygame import mixer
from gtts import gTTS
import allinone as ns
import time
import threading
import os

l1 = 0
lblTran = 0
t1 = 0
lblWelcome = 0
lblSpeak = 0
btnTH = 0
btnEN = 0
btnListen = 0
btnBack = 0


def play(text):
    mixer.init()
    mixer.music.load(text)
    mixer.music.play()


def delete(text):
    time.sleep(2)
    mixer.music.load("Holder.mp3")
    os.remove(text)


class PopupBox(Popup):
    pop_up_text = ObjectProperty()

    def update_pop_up_text(self, p_message):
        self.pop_up_text.text = p_message


class CustomDropDrown(BoxLayout):
    pass


class MyW(Widget):
    isShownMenu = True
    text = 'yay moo cow foo bar moo baa ' * 100

    def Label_Change(self, speechtext, speechLang):
        temp_str = []
        if speechtext != "" and speechtext != "too slow":
            temp_str = speechtext.split(',')
            # with open("speakThis.txt", "w") as text_file:
            #     print(speechtext, file=text_file)
            try:
                file = codecs.open("speakThis.txt", "w", "utf-8")
                try:
                    file.write(temp_str[0])
                except:
                    file.close()
                file.close()
                print(temp_str[0])
                lblSpeak.text = temp_str[0]
            finally:
                pass

            if temp_str[1] != "":
                result = temp_str[1]
                lblTran.text = result
        else:
            lblTran.text = 'too slow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #super(MyW, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init)

    def _finish_init(self, dt):
        global lblTran
        lblTran = self.ids.lblTran
        global t1
        t1 = self.ids.txb1
        global btnTH
        btnTH = self.ids.btnTH
        global btnEN
        btnEN = self.ids.btnEN
        global lblWelcome
        lblWelcome = self.ids.lblWelcome
        global lblSpeak
        lblSpeak = self.ids.lblSpeak
        global btnListen
        btnListen = self.ids.btnListen
        global btnBack
        btnBack = self.ids.btnBack


class ExampleApp(BoxLayout, App):
    kv_directory = "kvTemp"
    isShownMenu = True
    speakLang = ""

    def b_smash(self):
        self.ids.b1.text = 'Pudding'

    def process_button_click(self):
        # Open the pop up
        # play("start.mp3")
        self.show_popup()
        mythread = threading.Thread(
            target=self.something_that_takes_5_seconds_to_run)
        mythread.start()
        #verygood = ns.Test_Drive.test()
        # verygood = ns.Test_Drive.listen()
        # print(verygood)
        # print("asd")
        # MyW.Label_Change(self,verygood)
        # print("asd2")
        # self.pop_up.dismiss()

    def process_button_th(self):
        self.initiate_speech_recog("th")

    def process_button_en(self):
        self.initiate_speech_recog("en")

    def initiate_speech_recog(self, lang):
        self.speakLang = lang
        btnTH.opacity = 0
        btnTH.disabled = True
        btnEN.opacity = 0
        btnEN.disabled = True
        if (lang == "th"):
            lblWelcome.text = "ยินดีต้อนรับ"
            play('speakTH.mp3')
        if (lang == "en"):
            lblWelcome.text = "Welcome"
            play('speakEN.mp3')
        lblSpeak.opacity = 1
        lblTran.opacity = 1
        lblWelcome.opacity = 1
        btnListen.opacity = 1
        time.sleep(2)
        btnListen.disabled = False
        btnBack.opacity = 1
        btnBack.disabled = False
        pass

    def restore_main_menu(self):
        btnTH.opacity = 1
        btnTH.disabled = False
        btnEN.opacity = 1
        btnEN.disabled = False
        lblSpeak.opacity = 0
        lblTran.opacity = 0
        lblWelcome.opacity = 0
        btnListen.opacity = 0
        btnListen.disabled = True
        btnBack.opacity = 0
        btnBack.disabled = True

    def something_that_takes_5_seconds_to_run(self):
        translation = ns.listen(self.speakLang)
        if translation != "error1239123":
            print(translation)
            print("asd")
            MyW.Label_Change(self, translation, self.speakLang)
            print("asd2")
        else:
            if self.speakLang == 'th':
                errorsound = "errorTH.mp3"
            if self.speakLang == 'en':
                errorsound = "errorEN.mp3"
            play(errorsound)
            print("error")
        self.pop_up.dismiss()

    def show_popup(self):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_pop_up_text('Running some task...')
        self.pop_up.open()

    def build(self):
        # self.add_widget(MyW())
        # self.add_widget(CustomDropDown())
        # return self
        return MyW()


if __name__ == "__main__":
    try:
        ExampleApp().run()
    except KeyboardInterrupt:
        print("interrupt")
