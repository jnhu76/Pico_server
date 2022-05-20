from typing import List
from tortoise.contrib.pydantic import pydantic_model_creator

from core.models.images import Images


Image_Pydantic = pydantic_model_creator(Images, name="Image")
ImageIn_Pydantic = pydantic_model_creator(Images, name="ImageIn", exclude_readonly=True)
