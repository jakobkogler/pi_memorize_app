from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.clock import Clock
from reciter import Reciter
from time import sleep


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
        else:
            image = WrongDigitImage()
            self.add_widget(image)
            self.animate_grow(image)
            Clock.schedule_once(lambda _: self.remove_widget(image), .5)

    def update_correct_digits(self):
        self.correct_digits = 'Correct digits: {}'.format(self.reciter.pos)

    def animate_grow(self, instance):
        animation = Animation(size_hint=(.8, .8), duration=.5)
        animation.start(instance)


class WrongDigitImage(Image):
    pass


class MainApp(App):
    @staticmethod
    def build():
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
