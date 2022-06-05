from tortoise import fields, models


class Albums(models.Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256, null=False)
    user = fields.ForeignKeyField("models.images", related_name='user')
    text = fields.TextField()
    page = fields.ForeignKeyField("models.images", related_name='firstpage')
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "albums"
        table_description = "album models."