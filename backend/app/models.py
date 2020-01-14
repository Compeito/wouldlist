from tortoise import fields, models


class User(models.Model):
    uid = fields.CharField(pk=True, max_length=50)

    name = fields.CharField(max_length=50)
    photo_url = fields.CharField(max_length=255)
    screen_name = fields.CharField(max_length=20)

    access_token = fields.CharField(max_length=255)
    access_secret = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}(@{self.screen_name})'
