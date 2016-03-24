from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from src.reciter import Reciter


class ReciteScreen(Screen):
    """Screen for reciting pi"""

    pi_output = StringProperty('')
    correct_digits = StringProperty('')
    wrong_attempts = StringProperty('')

    def __init__(self, **kwargs):
        """Initialize everything and start calculating the first digits of pi."""
        super(ReciteScreen, self).__init__(**kwargs)
        self.reciter = Reciter()
        self.image = None
        self.allowed_errors = 3
        self.error_sound = SoundLoader.load('media/error.wav')
        self.reset()

    def digit_pressed(self, digit):
        """After pressing a digit on the screen, verify it and react to the result."""
        if not self.image:
            if self.reciter.check_next_digit(digit):
                self.pi_output += digit
                self.update_correct_digits()
            else:
                if self.reciter.errors > 3:
                    self.reset()
                else:
                    self.update_wrong_attempts()
                self.image = WrongDigitImage()
                self.add_widget(self.image)
                self.animate_grow(self.image)
                if self.error_sound:
                    self.error_sound.play()

    def update_correct_digits(self):
        """Display the current count of correct recited digits of pi."""
        self.correct_digits = 'Correct digits: {}'.format(self.reciter.pos)

    def update_wrong_attempts(self):
        """Displays the current number of wrong attempts."""
        self.wrong_attempts = 'Allowed errors: {}'.format(self.allowed_errors - self.reciter.errors)

    def animate_grow(self, instance):
        """Make an animation that grows an image from 0 to 100."""
        animation = Animation(size_hint=(1, 1), duration=.5)
        animation.bind(on_complete=self.remove_wrong_digit_image)
        animation.start(instance)

    def remove_wrong_digit_image(self, *_):
        """Remove the image, that is displayed when a wrong digits was inputted."""
        self.remove_widget(self.image)
        self.image = None

    def reset(self):
        """Reset the input field and the counts."""
        self.reciter.reset()
        self.update_correct_digits()
        self.update_wrong_attempts()
        self.pi_output = '3.'


class WrongDigitImage(Image):
    """"Class representing the image 'X.png', that is displayed after a wrong input."""
    pass
