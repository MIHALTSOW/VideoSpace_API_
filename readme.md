### Как зайти в приложение

1. собрать и запустить контейнеры `docker compose up`
2. в консоли вводим `docker exec -it django python manage.py shell`
3. далее в shell вводим (открывшееся окно)
`from Authorization_token.models import AuthorizationUserOnToken`
`AuthorizationUserOnToken.objects.create_superuser('alex', 'alex@alex.com', '123', is_staff=True)`
Можно ввести свои данные пользователя
`exit` - выходим из shell
4. переходим по адресу `http://localhost:3000/`
5. проходим авторизацию 
6. пользуемся сайтом
