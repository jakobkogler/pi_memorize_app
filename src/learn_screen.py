from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.properties import StringProperty, ObjectProperty
from src.reciter import Reciter
from pi_memorize.convert_to_major import ConverterMajorSystem
import os


class LearnScreen(Screen):
    """For learn the next few digits of pi."""

    def __init__(self, **kwargs):
        super(LearnScreen, self).__init__(**kwargs)


class LearnScreenManager(Carousel):
    """Carousel for displaying pi learning cards."""

    def __init__(self, **kwargs):
        """Initialize everything and create the first few slides."""
        super(LearnScreenManager, self).__init__(**kwargs)
        self.reciter = Reciter()
        path = os.path.join(os.path.dirname(__file__),
                            '..', 'pi_memorize', 'major1000.csv')
        self.converter = ConverterMajorSystem(path)
        self.add_new_slides()

    def slide_changed(self):
        """After the slides changed, check if it should generate more slides."""
        if self.index == len(self.slides) - 1:
            self.add_new_slides()

    def add_new_slides(self):
        """Adds 10 new slides to the carousel."""
        self.reciter.compute_pi(self.reciter.current_calculated + 150)
        for i in range(10):
            cur_len = 15*len(self.slides)
            digits = self.reciter.pi[cur_len:cur_len+15]
            output = self.converter.convert(digits)
            self.add_widget(LearnInfo(output, cur_len))

class LearnInfo(FloatLayout):
    """Displaying five new words."""

    label_text = StringProperty('')
    grid = ObjectProperty(None)

    def __init__(self, info, index, **kwargs):
        """"Initialize everything and create 5 lines."""
        super(LearnInfo, self).__init__(**kwargs)
        self.label_text = 'Digits {idx} to {idx2}:'.format(idx=index+1, idx2=index+15)

        for line in info:
            self.grid.add_widget(InfoLabel(text=line.digits))
            self.grid.add_widget(InfoLabel(text=line.words))


class InfoLabel(Label):
    """Modified label for displaying pi-digits and the converted words."""
