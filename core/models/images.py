from tortoise import fields, models


class Images(models.Model):
    """
    The Image model
    """

    uid = fields.UUIDField(pk=True)
    filename = fields.CharField(max_length=100)
    upload_name = fields.CharField(max_length=255)
    checksum = fields.CharField(max_length=255, index=True, unique=True)
    content_type = fields.CharField(max_length=255)
    metadata = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)
    is_deleted = fields.BooleanField(default=False)
    deleted_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "images"
        table_description = "image models."

    class PydanticMeta:
        exclude = ("created_at", "is_deleted", "deleted_at")
