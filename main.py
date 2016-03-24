from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from src.recite_screen import ReciteScreen


class RootWidget(FloatLayout):
    """Root widget for the app."""
    pass


class MainApp(App):
    """Class representing the app."""

    @staticmethod
    def build():
        """"Builds the app by creating a root widget."""
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
