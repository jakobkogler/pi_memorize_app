from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.carousel import Carousel
from kivy.properties import StringProperty


class LearnScreen(Screen):
    """For learn the next few digits of pi."""

    def __init__(self, **kwargs):
        super(LearnScreen, self).__init__(**kwargs)


class LearnScreenManager(Carousel):
    def __init__(self, **kwargs):
        super(LearnScreenManager, self).__init__(**kwargs)

        for i in range(1, 11):
            self.add_widget(LearnInfo(i))


class LearnInfo(FloatLayout):
    """Displaying five new words."""

    label_text = StringProperty('')

    def __init__(self, number, **kwargs):
        super(LearnInfo, self).__init__(**kwargs)
        self.label_text = str(number)
