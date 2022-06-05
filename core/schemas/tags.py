from tortoise.contrib.pydantic import pydantic_model_creator

from core.models.tags import Tags

Tags_Pydantic = pydantic_model_creator(Tags, name="Tag")