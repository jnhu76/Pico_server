from enum import unique
from tortoise import fields, models


class Tags(models.Model):
    """
    The tag model.
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)
    images = fields.ManyToManyField("models.images", related_name='images')
    user = fields.ForeignKeyField('models.users', related_name='user')
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
