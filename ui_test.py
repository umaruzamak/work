'''
Application built from a  .kv file
==================================

This shows how to implicitly use a .kv file for your application. You
should see a full screen button labelled "Hello from test.kv".

After Kivy instantiates a subclass of App, it implicitly searches for a .kv
file. The file test.kv is selected because the name of the subclass of App is
TestApp, which implies that kivy should try to load "test.kv". That file
contains a root Widget.
'''

import kivy
kivy.require('1.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Widgets(Widget):
    pass

    def getText(self):
        with open('showthisone.txt', 'r') as myfile:
            data = myfile.read().replace('\n', '')
        return "ๆีำรๆไำ่ๆกหฟ่ก"

    def Label_Change(self, speechtext):
        if speechtext != "":
            print(speechtext)
            self.ids.lbl.text = speechtext


class TestApp(App):
    kv_directory = 'template1'

    def build(self):
        return Widgets()


if __name__ == '__main__':
    TestApp().run()
