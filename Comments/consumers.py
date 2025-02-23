import json

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from Comments.models import CommentsPhoto


@sync_to_async
def get_user_username(comment):
    return comment.user.username


class CommentsPhotoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get('user', None)

        # Получаем id фото из URL, который передается через WebSocket
        self.photo_id = self.scope['url_route']['kwargs']['pk']

        # Формируем имя группы, в которой будут собираться все клиенты для данного фото
        self.group_name = f"photo_comments_{self.photo_id}"

        # Подключаем клиент к группе, чтобы обмениваться сообщениями
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Принимаем WebSocket-соединение с клиентом
        await self.accept()

    async def disconnect(self, close_code):
        # Отписываем клиента от группы при отключении
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        # Получаем данные от клиента (например, новый комментарий) и преобразуем в JSON
        data = json.loads(text_data)
        # Извлекаем текст комментария и id пользователя из данных
        comment_text = data.get('text')

        # Создаем новый комментарий в базе данных (выполняем синхронный запрос асинхронно)
        comment = await sync_to_async(CommentsPhoto.objects.create)(
            photo_id=self.photo_id,
            user_id=self.user.id,
            text=comment_text
        )
        # Отправляем новый комментарий всем подключенным клиентам в эту группу
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'new_comment',  # Тип события, по которому будет вызвана соответствующая функция
                'comment': comment.text,
                'user': await get_user_username(comment)
            }
        )

    async def new_comment(self, event):
        # Отправляем новый комментарий обратно всем подключенным клиентам через WebSocket
        await self.send(text_data=json.dumps({
            'user': event['user'],
            'comment': event['comment']
        }))
