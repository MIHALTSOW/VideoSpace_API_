Как откатить все миграции в БД, а также удалить все данные из БД

```shell
git pull
# обновить репозитории
```


```python
python manage.py showmigrations Authorization_token
# посмотреть на какой миграции ты сейчас 
# необязательно, просто для информации
```


```python
python manage.py flush
# удалить данные из БД
```


```python
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# удалить все миграции из кода, кроме __init__.py
```


```python
rm db.sqlite3
# удалить БД
```


```python
pip uninstall Django
# удалить Django
```


```python
pip install Django
# установить Django
```


```python
python manage.py makemigrations
# создать миграции
```


```python
python manage.py migrate
# применить миграции
```

# Данные обновлены в бд