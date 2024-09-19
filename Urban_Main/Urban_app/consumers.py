import json
from channels.generic.websocket import AsyncWebsocketConsumer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
channel_layer = get_channel_layer()

print('channel_layer',channel_layer)

from .views import Dashboard

class DashboardSocket(AsyncWebsocketConsumer):
    async def connect(self):
        print('.......connected')

        await self.channel_layer.group_add('str(machine_id)'+'_io', self.channel_name)

        await self.accept()


        try:

            dashboard_api_fun = await Dashboard()
            dashboard_api_fun_json = json.dumps({"dashboard_data":dashboard_api_fun})

            channel_layer = get_channel_layer()
            await channel_layer.group_send('str(machine_id)'+'_io',
                                           {"type": "dashboard_socket_data", "text": dashboard_api_fun_json})
        except Exception as e:
            status = json.dumps({"status": e})

            channel_layer = get_channel_layer()
            await channel_layer.group_send('str(machine_id)'+'_io',
                                           {"type": "dashboard_socket_data", "text": status})



    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('str(machine_id)'+'_io', self.channel_name)

    async def receive(self, text_data):

        await self.channel_layer.group_send('str(machine_id)'+'_io', {
            "type": "dashboard_socket_data",
            "text": text_data  # Send the processed data as the message
        })

    async def dashboard_socket_data(self, event):

        try:
            await self.send(text_data=event["text"])

        except Exception as e:
            print("chat message error - ", e)
