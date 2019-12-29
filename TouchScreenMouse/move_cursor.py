from rpyc.utils.server import ThreadedServer
from rpyc import Service
from win32api import SetCursorPos


class CuConServer(Service):
    def on_connect(self, conn):
        print('Connected :', conn)

    def on_disconnect(self, conn):
        print('Disconnected :', conn)

    def exposed_move_cursor(self, x_percent, y_percent):
        SetCursorPos((int(1366*x_percent), int(768*(1-y_percent))))


if __name__ == '__main__':
    server = ThreadedServer(CuConServer, port=7777)
    server.start()
