from drf_spectacular.utils import OpenApiResponse

user_logout = OpenApiResponse(
    description="Успешный ответ",
    response={
        "type": "object",
        "properties": {
            "success": {"type": "string"},
        }
    }
)

check_registration_key = OpenApiResponse(
    description="Успешный ответ",
    response={
        "type": "object",
        "properties": {
            "checkStatus": {"type": "boolean"}
        }
    }
)
