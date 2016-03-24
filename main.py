from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.animation import Animation
from reciter import Reciter


class RootWidget(FloatLayout):
    pass


class ReciteScreen(Screen):
    pi_output = StringProperty('3.')
    correct_digits = StringProperty('')

    def __init__(self, **kwargs):
        super(ReciteScreen, self).__init__(**kwargs)
        self.reciter = Reciter()
        self.image = None
        self.update_correct_digits()

    def digit_pressed(self, digit):
        if not self.image:
            if self.reciter.check_next_digit(digit):
                self.pi_output += digit
                self.update_correct_digits()
            else:
                self.image = WrongDigitImage()
                self.add_widget(self.image)
                self.animate_grow(self.image)

    def update_correct_digits(self):
        self.correct_digits = 'Correct digits: {}'.format(self.reciter.pos)

    def animate_grow(self, instance):
        animation = Animation(size_hint=(1, 1), duration=.5)
        animation.bind(on_complete=self.remove_wrong_digit_image)
        animation.start(instance)

    def remove_wrong_digit_image(self, *_):
        self.remove_widget(self.image)
        self.image = None


class WrongDigitImage(Image):
    pass


class MainApp(App):
    @staticmethod
    def build():
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
