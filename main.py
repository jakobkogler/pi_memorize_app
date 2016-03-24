from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.animation import Animation
from reciter import Reciter


class RootWidget(FloatLayout):
    """Root widget for the app."""
    pass


class ReciteScreen(Screen):
    """Screen for reciting pi"""

    pi_output = StringProperty('3.')
    correct_digits = StringProperty('')

    def __init__(self, **kwargs):
        """Initialize everything and start calculating the first digits of pi."""
        super(ReciteScreen, self).__init__(**kwargs)
        self.reciter = Reciter()
        self.image = None
        self.update_correct_digits()

    def digit_pressed(self, digit):
        """After pressing a digit on the screen, verify it and react to the result."""
        if not self.image:
            if self.reciter.check_next_digit(digit):
                self.pi_output += digit
                self.update_correct_digits()
            else:
                self.image = WrongDigitImage()
                self.add_widget(self.image)
                self.animate_grow(self.image)

    def update_correct_digits(self):
        """Display the current count of correct recited digits of pi."""
        self.correct_digits = 'Correct digits: {}'.format(self.reciter.pos)

    def animate_grow(self, instance):
        """Make an animation that grows an image from 0 to 100."""
        animation = Animation(size_hint=(1, 1), duration=.5)
        animation.bind(on_complete=self.remove_wrong_digit_image)
        animation.start(instance)

    def remove_wrong_digit_image(self, *_):
        """Remove the image, that is displayed when a wrong digits was inputted."""
        self.remove_widget(self.image)
        self.image = None


class WrongDigitImage(Image):
    """"Class representing the image 'X.png', that is displayed after a wrong input."""
    pass


class MainApp(App):
    """Class representing the app."""

    @staticmethod
    def build():
        """"Builds the app by creating a root widget."""
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
