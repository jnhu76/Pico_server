import mimetypes
import uuid
from datetime import datetime

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from tortoise.contrib.fastapi import HTTPNotFoundError

from core.models.images import Images
from core.schemas.images import Image_Pydantic
from core.services.storage.minio import get_file, upload_file

router = APIRouter()


@router.get(
    "/info/{checksum}",
    response_model=Image_Pydantic,
    name="image:get-image-information",
    responses={404: {"model": HTTPNotFoundError}},
)
async def retrieve_image_by_checksum(checksum: str):
    return await Image_Pydantic.from_queryset_single(Images.get(checksum=checksum))


@router.get(
    "/file/{checksum}",
    name="image:get-image",
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_image_stream(checksum: str):
    image = await Image_Pydantic.from_queryset_single(Images.get(checksum=checksum))
    return StreamingResponse(get_file(image.filename), media_type=image.content_type)


@router.post("/file", name="image:upload-image")
async def create_image(file: UploadFile = File(...)):
    try:
        # datetime + uuid + . + extension
        # 202205221522-138736483195bbcdcb104bee2f.jpg
        new_name = "{0}-{1}{2}".format(
            datetime.now().strftime("%Y%m%d"),
            (uuid.uuid4().hex)[6:],
            mimetypes.guess_extension(file.content_type),
        )
        ret = upload_file(new_name, file.file.fileno(), file.content_type)
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    image = await Images.create(
        filename=new_name,
        upload_name=file.filename,
        checksum=ret.etag,
        content_type=file.content_type,
    )
    return await Image_Pydantic.from_tortoise_orm(image)
