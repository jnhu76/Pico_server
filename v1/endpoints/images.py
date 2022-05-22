import io
import json
import mimetypes
import uuid
from datetime import datetime
from typing import Union

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from tortoise.contrib.fastapi import HTTPNotFoundError
from wand.image import Image

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
async def get_image_stream(
    checksum: str,
    h: Union[int, None] = None,
    w: Union[int, None] = None,
    sw: Union[int, None] = None,
    sh: Union[int, None] = None,
    cl: Union[int, None] = None,
    cr: Union[int, None] = None,
    ct: Union[int, None] = None,
    cb: Union[int, None] = None,
    b: Union[int, None] = None,
    br: Union[int, None] = None,
    bs: Union[int, None] = None,
    ab: Union[int, None] = None,
    abr: Union[int, None] = None,
    abs: Union[int, None] = None,
    g: Union[int, None] = None,
    gs: Union[int, None] = None,
    mb: Union[int, None] = None,
    mbr: Union[int, None] = None,
    mbs: Union[int, None] = None,
    mba: Union[int, None] = None,
    rb: Union[int, None] = None,
    rba: Union[int, None] = None,
    sharpen: Union[int, None] = None,
    sharpenr: Union[int, None] = None,
    sharpens: Union[int, None] = None,
    flip: Union[int, None] = None,
    flop: Union[int, None] = None,
    ro: Union[int, None] = None,
    f: Union[str, None] = None,
    q: Union[int, None] = 75,
):
    image = await Image_Pydantic.from_queryset_single(Images.get(checksum=checksum))
    content = get_file(image.filename)
    response_img = io.BytesIO()
    with Image(file=content) as img:
        if h or w:
            img.resize(
                width=w or image.metadata["weight"],
                height=h or image.metadata["height"],
            )
        if sh and sw:
            img.sample(width=sh, height=sw)
        if cl and ct and cr and cb:
            img.crop(cl, ct, cr, cb)
        if b and br and bs:
            # blur
            img.blur(radius=br, sigma=bs)
        if ab and abr and abs:
            # Adaptive Blur
            img.adaptive_blur(radius=abr, sigma=abs)
        if g and gs:
            img.gaussian_blur(sigma=gs)
        if mb and mbr and mbs and mba:
            # Motion Blur
            img.motion_blur(radius=mbr, sigma=mbs, angle=mba)
        if rb and rba:
            # Rotational Blur
            img.rotational_blur(angle=ra)
        if sharpen and sharpenr and sharpens:
            # sharpen
            img.sharpen(radius=sharpenr, sigma=sharpens)
        if flip:
            img.flip()
        if flop:
            img.flop()
        if ro:
            # rotate
            img.rotate(r)
        if f:
            img.format = f
        img.compression_quality = q
        img.save(file=response_img)
        response_img.seek(0)
    return StreamingResponse(response_img, media_type=image.content_type)


@router.post("/file", name="image:upload-image")
async def create_image(file: UploadFile = File(...)):
    try:
        metadata = {}
        with Image(file=file.file) as img:
            metadata["width"] = img.width
            metadata["height"] = img.height
            metadata["size"] = img.size
            metadata["format"] = img.format
        # datetime + uuid + . + extension
        # 202205221522-138736483195bbcdcb104bee2f.jpg
        new_name = "{0}-{1}{2}".format(
            datetime.now().strftime("%Y%m%d"),
            (uuid.uuid4().hex)[6:],
            mimetypes.guess_extension(file.content_type),
        )
        file.file.seek(0)
        ret = upload_file(new_name, file.file.fileno(), file.content_type)
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    image = await Images.create(
        filename=new_name,
        upload_name=file.filename,
        checksum=ret.etag,
        content_type=file.content_type,
        metadata=json.dumps(metadata),
    )
    return await Image_Pydantic.from_tortoise_orm(image)
