from tabnanny import check
from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse

from tortoise.contrib.fastapi import HTTPNotFoundError
from starlette.status import HTTP_400_BAD_REQUEST

from core.models.images import Images
from core.schemas.images import Image_Pydantic, ImageIn_Pydantic
from core.services.storage.minio import upload_file


router = APIRouter()

@router.get("/info/{checksum}", response_model=Image_Pydantic, name="image:get-image-information", responses={404: {"model": HTTPNotFoundError}})
async def retrieve_image_by_checksum(checksum: str):
    return await Image_Pydantic.from_queryset_single(Images.get(checksum=checksum))


@router.get("/file/{checksum}", name="image:get-image", responses={404: {"model": HTTPNotFoundError}})
async def get_image_stream(checksum: str):
    filename = await Image_Pydantic.from_queryset_single(Images.get(checksum=checksum))
    # todo: return minio file.
    return filename

@router.post("/file", name="image:upload-image")
async def create_image(file: UploadFile):
    ret = await upload_file(file.filename, file.file.fileno(), file.content_type)
    return {"filename": file.filename, "ret": ret}
