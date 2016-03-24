from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.carousel import Carousel
from kivy.properties import StringProperty
from src.reciter import Reciter
from pi_memorize.convert_to_major import ConverterMajorSystem


class LearnScreen(Screen):
    """For learn the next few digits of pi."""

    def __init__(self, **kwargs):
        super(LearnScreen, self).__init__(**kwargs)


class LearnScreenManager(Carousel):
    def __init__(self, **kwargs):
        super(LearnScreenManager, self).__init__(**kwargs)
        self.reciter = Reciter()
        self.converter = ConverterMajorSystem('../pi_memorize/major1000.csv')
        self.add_new_slides()

    def slide_changed(self):
        if self.index == len(self.slides) - 1:
            self.add_new_slides()

    def add_new_slides(self):
        self.reciter.compute_pi(self.reciter.current_calculated + 150)
        for i in range(10):
            cur_len = 15*len(self.slides)
            digits = self.reciter.pi[cur_len:cur_len+15]
            output = self.converter.convert(digits)
            self.add_widget(LearnInfo(output))

class LearnInfo(FloatLayout):
    """Displaying five new words."""

    label_text = StringProperty('')

    def __init__(self, info, **kwargs):
        super(LearnInfo, self).__init__(**kwargs)
        self.label_text = info[0].words
