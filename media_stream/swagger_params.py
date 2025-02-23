from drf_spectacular.utils import OpenApiParameter

video_photo_search_params = [
    OpenApiParameter(
        name='search',
        description='Поиск по полям title, description и category. Поддерживает частичное совпадение.',
        required=False,
        type=str
    ),
    OpenApiParameter(
        name='created_after',
        description='Фильтрация по дате создания (например, "gte=2023-01-01" для фильтрации по дате >= 2023-01-01).',
        required=False,
        type=str
    ),
    OpenApiParameter(
        name='created_before',
        description='Фильтрация по дате создания (например, "gte=2023-01-01" для фильтрации по дате >= 2023-01-01).',
        required=False,
        type=str
    ),
    OpenApiParameter(
        name='title',
        description='Фильтрация по названию. Поддерживает частичное совпадение.',
        required=False,
        type=str
    ),
    OpenApiParameter(
        name='category',
        description='Фильтрация по категории. Можно указать несколько категорий через запятую.',
        required=False,
        type=str
    ),
    OpenApiParameter(
        name='username',
        description='Фильтрация по имени пользователя. Поддерживает частичное совпадение (не обязательно соблюдать регистр).',
        required=False,
        type=str
    ),
    OpenApiParameter(
        name='user_id',
        description='Фильтрация по id пользователя. Обязательно точное совпадение.',
        required=False,
        type=int
    ),
]
