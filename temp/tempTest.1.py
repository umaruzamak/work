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
import nocsmspeech as ns
import nocsmtranslator as nt
import time
import threading
import os
import signal
import _signal

l1 = 0
lblTran = 0
t1 = 0
lblWelcome = 0
lblSpeak = 0
btnTH = 0
btnEN = 0
btnListen = 0


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


class Ticker(threading.Thread):
    """A very simple thread that merely blocks for :attr:`interval` and sets a
    :class:`threading.Event` when the :attr:`interval` has elapsed. It then waits
    for the caller to unset this event before looping again.

    Example use::

            t = Ticker(1.0) # make a ticker
            t.start() # start the ticker in a new thread
            try:
                    while t.evt.wait(): # hang out til the time has elapsed
                            t.evt.clear() # tell the ticker to loop again
                            print time.time(), "FIRING!"
            except:
                    t.stop() # tell the thread to stop
                    t.join() # wait til the thread actually dies

    """
    # SIGALRM based timing proved to be unreliable on various python installs,
    # so we use a simple thread that blocks on sleep and sets a threading.Event
    # when the timer expires, it does this forever.

    def __init__(self, interval):
        super(Ticker, self).__init__()
        self.interval = interval
        self.evt = threading.Event()
        self.evt.clear()
        self.should_run = threading.Event()
        self.should_run.set()

    def stop(self):
        """Stop the this thread. You probably want to call :meth:`join` immediately
        afterwards
        """
        self.should_run.clear()

    def consume(self):
        was_set = self.evt.is_set()
        if was_set:
            self.evt.clear()
        return was_set

    def run(self):
        """The internal main method of this thread. Block for :attr:`interval`
        seconds before setting :attr:`Ticker.evt`

        .. warning::
                Do not call this directly!  Instead call :meth:`start`.
        """
        while self.should_run.is_set():
            time.sleep(self.interval)
            self.evt.set()


class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(_signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


class MyW(Widget):
    isShownMenu = True

    stop = threading.Event()

    def start_second_thread(self, l_text):
        threading.Thread(target=self.second_thread, args=(l_text,)).start()

    def second_thread(self, label_text):
        # Remove a widget, update a widget property, create a new widget,
        # add it and animate it in the main thread by scheduling a function
        # call with Clock.
        Clock.schedule_once(self.start_test, 0)

        # Do some thread blocking operations.
        time.sleep(5)
        l_text = str(int(label_text) * 3000)

        # Update a widget property in the main thread by decorating the
        # called function with @mainthread.
        self.update_label_text(l_text)

        # Do some more blocking operations.
        time.sleep(2)

        # Remove some widgets and update some properties in the main thread
        # by decorating the called function with @mainthread.
        self.stop_test()

        # Start a new thread with an infinite loop and stop the current one.
        threading.Thread(target=self.infinite_loop).start()

    def infinite_loop(self):
        iteration = 0
        while True:
            if self.stop.is_set():
                # Stop running this thread so the main Python process can exit.
                return
            iteration += 1
            print('Infinite loop, iteration {}.'.format(iteration))
            time.sleep(1)

    def Label_Change(self, speechtext, speechLang):
        if speechtext != "":
            # with open("speakThis.txt", "w") as text_file:
            #     print(speechtext, file=text_file)
            try:
                file = codecs.open("speakThis.txt", "w", "utf-8")
                try:
                    file.write(speechtext)
                except:
                    file.close()
                file.close()
                print(speechtext)
                #t1.text = speechtext
                lblSpeak.text = speechtext
            finally:
                pass

        if speechtext != "":
            if speechLang == "th":
                result = nt.translateForMe("th", "en", speechtext)
                tts = gTTS(result, lang='en', slow=False)
            if speechLang == "en":
                result = nt.translateForMe("en", "th", speechtext)
                tts = gTTS(result, lang='th', slow=False)
            tts.save("testTran.mp3")
            play("testTran.mp3")
            # delete("testTran.mp3")
            lblTran.text = result

        # with open('showthisone.txt', 'r' , encoding='utf-8') as myfile:
        #     data = myfile.read().replace('\n', '')
        #     l2.text = data

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #super(MyW, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init)

    def _finish_init(self, dt):
        # global l1
        # l1 = self.ids.l1
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
        # etc


class ExampleApp(BoxLayout, App):
    kv_directory = "kvTemp"
    isShownMenu = True
    speakLang = ""
    toLang = ""
    textsp = ""

    def on_stop(self):
        # The Kivy event loop is about to stop, set a stop signal;
        # otherwise the app window will close, but the Python process will
        # keep running until all secondary threads exit.
        self.root.stop.set()

    def process_button_click(self):
        # Open the pop up
        # play("start.mp3")
        self.show_popup()
        mythread = threading.Thread(
            target=self.something_that_takes_5_seconds_to_run)
        mythread.start()
        mythread2 = threading.Thread(target=self.auto_dismiss)
        mythread2.start()
        #verygood = ns.Test_Drive.test()
        # verygood = ns.Test_Drive.listen()
        # print(verygood)
        # print("asd")
        # MyW.Label_Change(self,verygood)
        # print("asd2")
        # self.pop_up.dismiss()

    def auto_dismiss(self):
        time.sleep(30)
        self.pop_up.dismiss()

    def process_button_th(self):
        self.initiate_speech_recog("th")
        toLang = 'en'

    def process_button_en(self):
        self.initiate_speech_recog("en")
        toLang = 'th'

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
        pass

    def something_that_takes_5_seconds_to_run(self):

        Clock.schedule_once(self.start_listen, 0.5)
        verygood = self.textsp
        if verygood != "error1239123":
            print(verygood)
            print("asd")
            MyW.Label_Change(self, verygood, self.speakLang)
            print("asd2")
        else:
            if self.speakLang == 'th':
                errorsound = "errorTH.mp3"
            if self.speakLang == 'en':
                errorsound = "errorEN.mp3"
            play(errorsound)
            print("error")
        self.pop_up.dismiss()

    def start_listen(self, dt):
        if self.speakLang == "th":
            verygood = ns.Test_Drive.listen()
        else:
            verygood = ns.Test_Drive.listenEN()
        self.textsp = verygood

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
    ExampleApp().run()
