import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Custom command to update requirements, apply migrations, and start the Django server.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Устанавливаем зависимости из requirements.txt...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"])

        self.stdout.write("Применяем миграции...")
        subprocess.run(["python", "manage.py", "makemigrations"])
        subprocess.run(["python", "manage.py", "migrate"])

        self.stdout.write("Запускаем сервер Django...")
        subprocess.run(["python", "manage.py", "runserver"])
