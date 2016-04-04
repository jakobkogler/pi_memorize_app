from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from src.reciter import Reciter
from datetime import datetime


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
        self.correct = 0
        self.reset()

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
                if self.error_sound:
                    self.error_sound.play()
                self.correct = self.reciter.pos
                self.update_wrong_attempts()


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
        if self.reciter.errors == 3:
            self.reset()
            display = self.parent.hs_screen.hs_display
            if display.highscore.in_top_10(self.correct):
                popup = AskNamePopup(display, self.correct, datetime.now().strftime('%d.%m.%Y'), self.switch_to_highscore)
                popup.open()
            else:
                popup = NotInTop10Popup()
                popup.open()

    def reset(self):
        """Reset the input field and the counts."""
        self.reciter.reset()
        self.update_correct_digits()
        self.update_wrong_attempts()
        self.pi_output = '' # for reseting the cursor!
        self.pi_output = '3.'

    def switch_to_highscore(self):
        """Switch to the highscore screen."""
        self.parent.transition.direction = 'left'
        self.parent.current = 'highscore_screen'


class WrongDigitImage(Image):
    """"Class representing the image 'X.png', that is displayed after a wrong input."""
    pass


class AskNamePopup(Popup):
    """Ask for the name of the player."""

    def __init__(self, display, correct, date, switch_to_highscore, **kwargs):
        """Initializes everything."""
        super(AskNamePopup, self).__init__(**kwargs)
        self.display = display
        self.correct = correct
        self.date = date
        self.switch_to_highscore = switch_to_highscore

    def add_result(self, name):
        """Adds a result to the highscore and updates the highscore screen."""
        entry = (self.correct, name, self.date)
        self.display.highscore.add_result(*entry)
        self.display.load_highscore()
        self.dismiss()
        self.switch_to_highscore()


class NotInTop10Popup(Popup):
    """Tell the player that he didn't made it into the top 10."""
    pass
