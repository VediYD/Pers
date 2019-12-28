from kivy.app import App
from kivy.uix.widget import Widget


# class to define the widget
class TouchInput(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        print('DOWN>>', touch.sx, touch.sy, touch.sz)

    def on_touch_up(self, touch):
        print('UP>>', touch.sx, touch.sy, touch.sz)

    def on_touch_move(self, touch):
        print('MOVING>>', touch.sx, touch.sy, touch.sz)


# class to build the app
class KivyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        # creates an object of TouchInput class and returns it
        return TouchInput()


# main loop
if __name__ == '__main__':
    KivyApp().run()
