from tortoise import fields, models


class Users(models.Model):
    """
    The User model.
    """

    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=128, null=True)
    email = fields.CharField(max_length=256, null=True)
    phone = fields.CharField(max_length=16, null=True)
    info = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modefied_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"
        table_description = "user models."

    class PydanticMeta:
        exclude = ["password_hash"]


    