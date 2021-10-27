import json
import requests
import websocket
from threading import Thread

from .local import Local
from .lib import Event, UserInfo, CheckExceptions
from sys import _getframe as getframe

# By SirLez
# Solved By SirLez
# and Sloved By Bovonos ،_،
# and Reworked By SirLez ._.
# Note: socket2 is a socket to send & recv data ! ( Do Not load the data with json )


class Socket:
    def __init__(self, client):
        self.socket_url = "wss://ws1.narvii.com"
        self.client = client
        websocket.enableTrace(False)

    def handle_message(self, data):
        self.client.handle(data)
        return

    def on_error(self, error): print(error)
    def on_close(self): print("__CLOSED__")
    def send(self, data): self.socket2.send(json.dumps(data))
    def recv(self): return json.loads(self.socket2.recv())

    def web_socket_url(self):
        req = requests.get("https://aminoapps.com/api/chat/web-socket-url", headers={'cookie': self.client.sid})
        if req.status_code != 200: return CheckExceptions(req.json())
        else:
            self.socket_url = req.json()["result"]["url"]
            return self.socket_url
 
    def launch(self, socket2: bool = False):
        self.headers = {'cookie': self.client.sid}
        
        if socket2:
            self.socket2 = websocket.WebSocket()
            self.socket2.connect(self.web_socket_url(), header=self.headers)
            
        self.socket = websocket.WebSocketApp(
            self.web_socket_url(),
            on_message=self.handle_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header=self.headers
        )
        Thread(target=self.socket.run_forever, kwargs={"ping_interval": 60}).start()
        print("ready!")


class Recall:
    def __init__(self):
        global Client
        self.handlers = {}
        self.chat_methods = {
            "0:0": self.on_message,
            "3:113": self.on_sticker,
            "101:0": self.on_member_join,
            "102:0": self.on_member_left,
            "103:0": self.on_start_chat,
            "105:0": self.on_title_changed,
            "113:0": self.on_content_changed,
            "114:0": self.on_live_mode_started,
            "115:0": self.on_live_mode_ended,
            "116:0": self.on_host_changed,
            "118:0": self.on_left_chat,
            "120:0": self.on_chat_donate,
            "125:0": self.on_view_mode_enabled,
            "126:0": self.on_view_mode_disabled
        }
        self.notif_methods = {
            "53": self.on_set_you_host,
            "67": self.on_set_you_cohost,
            "68": self.on_remove_you_cohost
        }
        self.methods = {
            1000: self.chat_messages,
            10: self.payload,
        }

    def payload(self, data):
        value = f"{data['o']['payload']['notifType']}"
        return self.notif_methods.get(value, self.classic)(data)

    def chat_messages(self, data):
        value = f"{data['o']['chatMessage']['type']}:{data['o']['chatMessage'].get('mediaType', 0)}"
        return self.chat_methods.get(value, self.classic)(data)

    def solve(self, data):
        try: data = json.loads(data)
        except: data = data
        typ = data["t"]
        return self.methods.get(typ, self.classic)(data)

    def roll(self, func, data):
        if func in self.handlers:
            for handler in self.handlers[func]: handler(data)

    def event(self, func):
        def regHandler(handler):
            if func in self.handlers: self.handlers[func].append(handler)
            else: self.handlers[func] = [handler]
            return handler
        return regHandler

    def on_content_changed(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_view_mode_disabled(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"])) 
    def on_view_mode_enabled(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_live_mode_ended(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_live_mode_started(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_sticker(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_set_you_host(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_remove_you_cohost(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_host_changed(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_set_you_cohost(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_title_changed(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_left_chat(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_start_chat(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_chat_donate(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_member_join(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_member_left(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def on_message(self, data): self.roll(getframe(0).f_code.co_name, Event(data["o"]))
    def classic(self, data): self.roll(getframe(0).f_code.co_name, data)
