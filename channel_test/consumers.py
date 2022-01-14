from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class TestSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("received", event)

        self.send({
            'type': 'websocket.send',
            'text': 'thanks',
        })

    def websocket_disconnect(self, event):
        print("disconnected", event)
        # Without stop consumer the disconnect will be a infinite loop
        raise StopConsumer()


class TestAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("async connected", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("async received", event)

        await self.send({
            'type': 'websocket.send',
            'text': 'thanks from async',
        })

    async def websocket_disconnect(self, event):
        print("async disconnected", event)
        # Without stop consumer the disconnect will be a infinite loop
        raise StopConsumer()
