import json

import asyncio
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

from .models import File

class ShareConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connect',event)

        self.chat_room = 'share_app'
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name #defualt
        )

        await self.send({
            "type":'websocket.accept'
        })

        # await asyncio.sleep(10)
        # await self.send({
        #     'type': 'websocket.send',
        #     'text': 'Hello world'
        # })

    async def websocket_receive(self, event):
        print('receive', event)
        front_text = event.get('text',None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')

            myResponse = {
                'message': msg,
            }
            await self.create_file(msg)
            await self.channel_layer.group_send(
                self.chat_room,
                {
                    'type': 'chat_message',
                    'text':  json.dumps(myResponse)
                }
            )
            # print(msg)

    async def chat_message(self, event):
        # send the actual message
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    async def websocket_disconnect(self, event):
        print('disconnected', event)

    @database_sync_to_async
    def create_file(self, file):
        return File.objects.create(file=file)
