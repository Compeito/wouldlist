from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    screen_name = fields.CharField(max_length=20)
    description = fields.TextField()

    def __str__(self) -> str:
        return f'{self.name}(@{self.screen_name})'
