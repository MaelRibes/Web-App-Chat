import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data_json = json.loads(text_data)
        content = data_json["content"]
        username = data_json["username"]
        date = data_json["date"]
        self.send(text_data=json.dumps(
            {"username": username, "content": content, "date": date}))
