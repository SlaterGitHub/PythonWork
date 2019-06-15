import kivy.app
import kivy.uix.boxlayout as bx
import kivy.uix.textinput as inp
import kivy.uix.label as lbl
import kivy.uix.button as btn

class AndroidApp(kivy.app.App):
    def build(self):
        self.textInput = inp.TextInput()
        self.label = lbl.Label(text="Your Message")
        self.button = btn.Button(text="Click Me")
        self.button.bind(on_press = self.displayMessage)
        self.boxLayout = bx.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(self.textInput)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)
        return self.boxLayout
    def displayMessage(self, bn):
        self.label.text = self.textInput.text

if __name__ == "__main__":
    droid = AndroidApp()
    droid.run()
