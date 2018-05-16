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
import nocsmspeech

import time, threading

class PopupBox(Popup):
    pop_up_text = ObjectProperty()
    def update_pop_up_text(self, p_message):
        self.pop_up_text.text = p_message
   

class ExampleApp(App):
    kv_directory = "abcLocation2"
    

    def show_popup(self):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_pop_up_text('Running some task...')
        self.pop_up.open()

    def process_button_click(self):
        # Open the pop up
        self.show_popup()
        mythread = threading.Thread(target=self.something_that_takes_5_seconds_to_run)
        mythread.start()
        #Widgets.Label_Change(Widgets.sayHi(self))
        # Call some method that may take a while to run.
        # I'm using a thread to simulate this

    def something_that_takes_5_seconds_to_run(self):
        thistime = time.time() 
        # while thistime + 5 > time.time(): # 5 seconds
        #     time.sleep(1)
        #data = nocsmspeech.Test_Drive.listen()
        print("data")
        ExampleApp.Label_Change(self,"data")
        # Once the long running task is done, close the pop up.
        #self.pop_up.dismiss()
    

if __name__ == "__main__":
    ExampleApp().run()