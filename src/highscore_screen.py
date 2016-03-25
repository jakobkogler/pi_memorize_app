from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from src.highscore import HighScore
import os


class HighScoreScreen(Screen):
    """Screen displaying the current highscore."""

    hs_display = ObjectProperty(None)


class HighScoreDisplay(GridLayout):
    """Displays the current highscore."""

    def __init__(self, **kwargs):
        super(HighScoreDisplay, self).__init__(**kwargs)
        path = os.path.join(os.path.dirname(__file__), '..', 'highscore.csv')
        self.highscore = HighScore(path)
        self.load_highscore()

    def load_highscore(self):
        self.clear_widgets()
        highscore = self.highscore.highscore
        while len(highscore) < 10:
            highscore.append(['-', '-', '-'])
        for pos, (result, name, date) in enumerate(highscore[:10], start=1):
            self.add_widget(Label(text='{}.'.format(pos)))
            self.add_widget(Label(text=result))
            self.add_widget(Label(text=name))
            self.add_widget(Label(text=date))
