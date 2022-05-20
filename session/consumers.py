import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Session,SessionComment
from channels.db import database_sync_to_async


class SessionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['session_id']

        self.room_group_name = str(self.group_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.notify_home(notification_type='user_connect',content='')

        await self.notification_user_connect();

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

        #ユーザ退出通知
        # await self.notify_home(notification_type='user_disconnect',content='')

    '''js(websocket)から受信 & groupに送信'''
    async def receive(self,text_data):
        receive_data_json = json.loads(text_data)
        receive_data = receive_data_json['comment']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'post_user_information':{"nick_name":self.scope['user'].nick_name},
                'comment':receive_data,
            }
        )

        await self.notify_home(notification_type='comment',content=receive_data)

    async def user_connect(self,event):
        await self.send(text_data=json.dumps({
            "type":"user_connect",
        }))

    #groupから受信 & js(websocket)に送信
    async def chat_message(self,event):
        comment = event['comment']
        post_user_information = event['post_user_information']

        await self.send(text_data=json.dumps({
            "type":"comment",
            'comment':comment,
            'post_user_information':post_user_information,
        }))

        await self.store_session_comment(session_id=self.room_group_name,comment=comment)

    async def notify_home(self,notification_type,content):
        await self.channel_layer.group_send(
            str("global_group"),
            {
                'type':'notification',
                'notification_type':notification_type,
                'content':content,
                'session_id':self.room_group_name,
                'session_name':await self.get_session_name(session_id=self.room_group_name)
            }
        )

    async def notification_user_connect(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'user_connect',
                'connect_user_nick_name':'test',
            }
        )

    @database_sync_to_async
    def get_session_name(self,session_id):
        return Session.objects.get(pk=session_id).session_name

    @database_sync_to_async
    def store_session_comment(self,session_id,comment):
        #sessionインスタンスの取得
        session_instance = Session.objects.get(pk=session_id)

        new_comment = SessionComment(created_by=self.scope['user'],comment=comment,session_id=session_instance,created_by_nick_name=self.scope['user'].nick_name)
        new_comment.save()
