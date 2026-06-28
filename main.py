from kivy.app import App
from kivy.uix.webview import WebView
from kivy.core.window import Window

class AngerApp(App):
    def build(self):
        # Открываем сайт на весь экран
        return WebView(url='https://angerai.fun')

if __name__ == '__main__':
    AngerApp().run()
    