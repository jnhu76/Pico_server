from typing import BinaryIO

from core.models.images import Images
from core.services.storage.hash import get_hash, get_md5, get_sha1


async def check_image_is_in_pico(file: BinaryIO) -> bool:
    checksum = get_md5(file)
    return await Images.exists(checksum=checksum)