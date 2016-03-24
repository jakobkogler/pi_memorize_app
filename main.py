from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from reciter import Reciter


class RootWidget(FloatLayout):
    pass


class ReciteScreen(Screen):
    pi_output = StringProperty('3.')
    correct_digits = StringProperty('')

    def __init__(self, **kwargs):
        super(ReciteScreen, self).__init__(**kwargs)
        self.reciter = Reciter()
        self.update_correct_digits()

    def digit_pressed(self, digit):
        if self.reciter.check_next_digit(digit):
            self.pi_output += digit
            self.update_correct_digits()

    def update_correct_digits(self):
        self.correct_digits = 'Correct digits: {}'.format(self.reciter.pos)


class MainApp(App):
    @staticmethod
    def build():
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
