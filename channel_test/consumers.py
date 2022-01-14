import json

from channels.consumer import SyncConsumer, AsyncConsumer


class TestSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected", event)
        return True

    def websocket_receive(self, text_data):
        print("received", text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(json.dumps({
            'message': message
        }))

    def websocket_disconnect(self, event):
        print("disconnected", event)


class TestAsyncConsumer(AsyncConsumer):
    def websocket_connect(self, event):
        print("async connected", event)

    def websocket_receive(self, event):
        print("async received", event)

    def websocket_disconnect(self, event):
        print("async disconnected", event)
