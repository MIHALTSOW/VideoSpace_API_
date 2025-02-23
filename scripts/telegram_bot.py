import os

from asgiref.sync import sync_to_async

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VideoSpace_API.settings")

import sys

import django

sys.path.insert(0, "/code")

django.setup()

from telegram import Bot, Update
from telegram.ext import Application, CallbackContext, CommandHandler

from Authorization_token.models import (
    AuthorizationUserOnToken,
    TokenForRegistration,
)


# Асинхронная функция для отправки сообщения пользователю по chat_id
async def send_message(chat_id: str, message: str) -> None:
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


@sync_to_async
def create_token_for_registration(chat_id: str):
    user = AuthorizationUserOnToken.objects.create()
    registration_token = TokenForRegistration.objects.create(
        user=user, chat_id=chat_id
    )
    return registration_token


@sync_to_async
def try_get_telegram_name(update: Update, chat_id: str):
    try:
        telegram_username = update.message.from_user.username
        if telegram_username is None:
            return "У пользователя нет имени пользователя"
        TokenForRegistration.objects.update_or_create(
            chat_id=chat_id, defaults={"telegram_username": telegram_username}
        )
    except AttributeError as e:
        return "Не удалось получить имя пользователя, ошибка %s" % e


async def start(update: Update, context: CallbackContext) -> None:
    # Получаем уникальный идентификатор пользователя (chat_id) из объекта update
    chat_id = str(update.message.chat_id)
    token_info = await create_token_for_registration(chat_id=chat_id)
    telegram_name = await try_get_telegram_name(update, chat_id)

    # message = f"http://localhost:8000/api/registration/?key={token_info.registration_token}"
    message = f"http://localhost:5173/registration?key={token_info.registration_token}"
    # Вызываем функцию send_message, чтобы отправить дополнительное сообщение
    await send_message(chat_id, message)


def run_bot():
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    # Создаем объект Application для управления ботом, используя предоставленный токен
    application = Application.builder().token(bot_token).build()
    # Добавляем обработчик команды /start: при ее вызове будет запускаться функция start
    application.add_handler(CommandHandler("start", start))
    # Запускаем бот в режиме polling с использованием asyncio
    application.run_polling()


if __name__ == "__main__":
    run_bot()

# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         bot_token = '8199155454:AAFDI6xdgYH81_BNKEjELIuWM72N3-HUFdU'  # Замените на свой токен
#         # Создаем объект Application для управления ботом, используя предоставленный токен
#         application = Application.builder().token(bot_token).build()
#
#         # Асинхронная функция для отправки сообщения пользователю по chat_id
#         async def send_message(bot: Bot, chat_id: str, message: str) -> None:
#             # Создаем объект Bot с использованием токена, чтобы отправить сообщение
#             await bot.send_message(chat_id=chat_id, text=message)
#
#             # Асинхронная функция для обработки команды /start
#         async def start(update: Update, context: CallbackContext) -> None:
#             # Получаем уникальный идентификатор пользователя (chat_id) из объекта update
#             chat_id = str(update.message.chat_id)
#             token_info = TokenForRegistration.objects.create(user_id=chat_id)
#             message = f"http://localhost:8000/api/registration/?key={token_info.registration_token}"
#             # Вызываем функцию send_message, чтобы отправить дополнительное сообщение
#             bot_token = '8199155454:AAFDI6xdgYH81_BNKEjELIuWM72N3-HUFdU'  # Замените на свой токен
#             bot = Bot(token=bot_token)
#             await send_message(bot, chat_id, message)
#
#         # Добавляем обработчик команды /start: при ее вызове будет запускаться функция start
#         application.add_handler(CommandHandler('start', self.start))
#         # Запускаем бот в режиме polling, чтобы он принимал и обрабатывал входящие команды
#         application.run_polling()
#         logger.info("Бот успешно запущен")

# bot_token = '8199155454:AAFDI6xdgYH81_BNKEjELIuWM72N3-HUFdU'  # Замените на свой токен
# # Создаем объект Application для управления ботом, используя предоставленный токен
# application = Application.builder().token(bot_token).build()
#
# # Асинхронная функция для отправки сообщения пользователю по chat_id
# async def send_message(chat_id: str, message: str) -> None:
#     # Создаем объект Bot с использованием токена, чтобы отправить сообщение
#     bot = Bot(token=bot_token)
#     await bot.send_message(chat_id=chat_id, text=message)
#
#
# # Асинхронная функция для обработки команды /start
# async def start(update: Update, context: CallbackContext) -> None:
#     # Получаем уникальный идентификатор пользователя (chat_id) из объекта update
#     chat_id = str(update.message.chat_id)
#     message = 'Hello, do you want to get a token?'
#     # Отправляем ответ пользователю, информируя его о его chat_id
#     await update.message.reply_text(f"Ваш chat_id: {chat_id}")
#     # Вызываем функцию send_message, чтобы отправить дополнительное сообщение
#     await send_message(chat_id, message)
#
#
# # Добавляем обработчик команды /start: при ее вызове будет запускаться функция start
# application.add_handler(CommandHandler('start', start))
# # Запускаем бот в режиме polling, чтобы он принимал и обрабатывал входящие команды
# application.run_polling()
