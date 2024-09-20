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
        print('.......connected', self.channel_name)

        await self.channel_layer.group_add("singlemachine", self.channel_name)
        await self.accept()
        try:

            dashboard_api_fun = await Dashboard()
            # print('dashboard_api_fun',dashboard_api_fun)
            # dashboard_api_fun_data = dashboard_api_fun.content.decode('utf-8')  # Decode byte content to string

            # dashboard_data = dashboard_api_fun.json()
            # print('dashboard_data',dashboard_data)

            dashboard_api_fun_json = json.dumps(dashboard_api_fun)

            channel_layer = get_channel_layer()
            await channel_layer.group_send('singlemachine',
                                           {"type": "dashboardsocketdata", "text": dashboard_api_fun_json})
        except Exception as e:
            status = json.dumps({"status": e})

            channel_layer = get_channel_layer()
            await channel_layer.group_send('singlemachine',
                                           {"type": "dashboardsocketdata", "text": status})



    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('singlemachine', self.channel_name)

    async def receive(self, text_data):

        await self.channel_layer.group_send('singlemachine', {
            "type": "dashboardsocketdata",
            "text": text_data  # Send the processed data as the message
        })

    async def dashboardsocketdata(self, event):

        try:
            await self.send(text_data=event["text"])

        except Exception as e:
            print("dashboardsocketdata error - ", e)
