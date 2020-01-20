from typing import Tuple

from tortoise import fields, models

from app.utils import SerializableMixin


class User(SerializableMixin, models.Model):
    uid = fields.CharField(pk=True, max_length=50)

    name = fields.CharField(max_length=50)
    screen_name = fields.CharField(max_length=20)
    photo_url = fields.CharField(max_length=255)

    def get_serialize_fields(self) -> Tuple[str, ...]:
        return 'name', 'photo_url', 'screen_name'

    def __str__(self) -> str:
        return f'{self.name}(@{self.screen_name})'


class Todo(SerializableMixin, models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User')
    title = fields.CharField(max_length=100)
    text = fields.TextField()

    def get_serialize_fields(self) -> Tuple[str, ...]:
        return 'id', 'title', 'text'

    def __str__(self) -> str:
        return f'{self.user.name}さんのTODO: {self.title}'
