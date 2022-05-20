from channels.generic.websocket import AsyncWebsocketConsumer
import json

class HomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.group_name = 'global_group'
        self.room_group_name = self.group_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def notification(self,event):

        content = event['content']
        notification_type = event['notification_type']
        try:
            session_name = event['session_name']
            session_id = event['session_id']
        except:
            pass

        await self.send(text_data=json.dumps({
            'content':content,
            'notification_type':notification_type,
            'session_id':session_id,
            'session_name':session_name,
        }))
