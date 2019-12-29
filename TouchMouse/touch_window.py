from kivy.app import App
from kivy.uix.widget import Widget
from rpyc import connect


# class to define the widget
class TouchInput(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_connection = connect('localhost', 7777)

    def on_touch_down(self, touch):
        print('DOWN>>', touch.sx, touch.sy)
        self.server_connection.root.move_cursor(touch.sx, touch.sy)

    def on_touch_up(self, touch):
        print('UP>>', touch.sx, touch.sy)
        self.server_connection.root.move_cursor(touch.sx, touch.sy)

    def on_touch_move(self, touch):
        print('MOVING>>', touch.sx, touch.sy)
        self.server_connection.root.move_cursor(touch.sx, touch.sy)


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
