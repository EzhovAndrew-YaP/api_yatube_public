from rest_framework.serializers import SlugRelatedField

USER_DOES_NOT_EXIST_MESSAGE = (
    'Пользователь с {slug_name}={value} не существует.'
)
INVALID_VALUE = 'Недопустимое значение для поля username'


class MySlugRelatedField(SlugRelatedField):
    default_error_messages = {
        'does_not_exist': USER_DOES_NOT_EXIST_MESSAGE,
        'invalid': INVALID_VALUE
    }
