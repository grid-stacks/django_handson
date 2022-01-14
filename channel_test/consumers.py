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


class MqttConsumer(SyncConsumer):
    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        print("l51 consumers sub =======================================")
        print('subscribed.......................')
        print('topic', topic)
        print('payload', payload)

    def mqtt_pub(self, event):
        print("l57 consumers pub =======================================")
        print('publish', event)
        topic = event['text']['topic']
        payload = event['text']['payload']
        print("topic: {0}, payload: {1}".format(topic, payload))
