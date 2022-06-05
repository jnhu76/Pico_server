from tortoise.contrib.pydantic import pydantic_model_creator

from core.models.users import Users

User_Pydantic = pydantic_model_creator(Users, name="Users")
UserIn_Pydantic = pydantic_model_creator(Users, name="UsersIn", exclude_readonly=True)
