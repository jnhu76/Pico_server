from tortoise.contrib.pydantic import pydantic_model_creator

from core.models.albums import Albums


Album_Pydantic = pydantic_model_creator(Albums, name="Album")
