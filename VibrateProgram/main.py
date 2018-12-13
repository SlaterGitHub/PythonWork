import kivy.app
import kivy.uix.boxlayout as bx
import kivy.uix.textinput as inp
import kivy.uix.label as lbl
import kivy.uix.button as btn
import kivy.uix.popup as pup
from plyer import vibrator
import random  as rdm
from threading import Thread
import socket as sk

class AndroidApp(kivy.app.App):
    def build(self):
        self.l = False
        self.textInput = inp.TextInput()
        self.label = lbl.Label(text="")

        self.popText = lbl.Label(text="Make sure you are connected", font_size = '25sp')
        self.popBtn = btn.Button(text="Close", size_hint = (1, .5), size = (400, 50))
        self.box = bx.BoxLayout(orientation='vertical')
        self.box.add_widget(self.popText)
        self.box.add_widget(self.popBtn)
        self.popup = pup.Popup(title = "Error",
                               content=self.box,
                               auto_dismiss=False,
                               size_hint=(None, None),
                               size = (400,200)
                               )
        self.popBtn.bind(on_press=self.popup.dismiss)

        self.button = btn.Button(text="Connect", size_hint=(1,.25))
        self.button.bind(on_press = lambda x:self.conn(self.ip, self.button))

        """self.button2 = btn.Button(text="up")
        self.button2.bind(on_press = lambda x:self.sendMessage('up'))
        self.button2.bind(on_release = lambda x:self.sendMessage('stop'))

        self.button3 = btn.Button(text="down")
        self.button3.bind(on_release = lambda x:self.sendMessage('stop'))
        self.button3.bind(on_press = lambda x:self.sendMessage('down'))

        self.button4 = btn.Button(text="right")
        self.button4.bind(on_press = lambda x:self.sendMessage('right'))
        self.button4.bind(on_release = lambda x:self.sendMessage('stop'))
        
        self.button5 = btn.Button(text="left")
        self.button5.bind(on_press = lambda x:self.sendMessage('left'))
        self.button5.bind(on_release = lambda x:self.sendMessage('stop'))"""

        self.ip = inp.TextInput(text="enter ip to connect to", size_hint=(1,.25))

        self.textInput = inp.TextInput(size_hint=(1,.4))
        self.send = btn.Button(text="send message", size_hint=(1,.25))
        self.send.bind(on_press = lambda x:self.sendMessage(self.textInput))
        

        self.boxLayout = bx.BoxLayout(orientation="vertical")
        #self.boxLayout.add_widget(self.textInput)
        #self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.ip)
        self.boxLayout.add_widget(self.button)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.textInput)
        self.boxLayout.add_widget(self.send)

        
        #self.box1 = bx.BoxLayout(orientation = "vertical")
        """self.box1.add_widget(self.button2)
        self.box1.add_widget(self.button3)
        self.box2 = bx.BoxLayout(orientation = "horizontal")
        self.box2.add_widget(self.button5)
        self.box2.add_widget(self.box1)
        self.box2.add_widget(self.button4)
        self.boxLayout.add_widget(self.box2)"""
        
        return self.boxLayout
    def sendMessage(self, text):
        try:
            self.c.sendall(text)
            text = text + "\n"
            self.chatLog += text
            self.label.text = self.chatLog
            vibrator.vibrate(0.01)

        except:
            self.popup.open()
            vibrator.vibrate(3)

    def connect(self):
        self.m = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.m.bind(("localhost", 5000))
        self.m.listen(10)
        self.c, addr = self.m.accept()
        print("{} connected".format(addr))
        vibrator.vibrate(0.01)
        
    def conListen(self, sock, bn):
        while True:
            try:
                self.s.connect((sock, 5000))
                self.connect()
                self.thrd.join()
                break
            except:
                None
    def conn(self, sock, bn):
        self.thrd = Thread(target = self.conListen, args = (sock, bn))
        self.thrd.start()
        self.button.disabled = True
            

if __name__ == "__main__":
    droid = AndroidApp()
    droid.run()

