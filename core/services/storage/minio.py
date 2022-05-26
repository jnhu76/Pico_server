from typing import Dict, List

from minio import Minio
from minio.error import InvalidResponseError

from core.config import get_app_settings

settings = get_app_settings()
bucket = settings.MINIO_BUCKET

# create minio client
def get_minio_client() -> Minio:
    minio = Minio(
        settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=False,
    )
    return minio


def create_bucket() -> bool:
    minio: Minio = get_minio_client()

    if minio.bucket_exists(bucket):
        return False
    minio.make_bucket(bucket)


def remote_bucket() -> bool:
    minio: Minio = get_minio_client()

    # todo: remove all files.

    minio.remote_bucket(bucket)


# upload file
def upload_file(
    object_name: str, file_path: str, content_type: str, metadata: Dict = {}
):
    minio: Minio = get_minio_client()

    try:
        ret = minio.fput_object(
            bucket_name=bucket,
            object_name=object_name,
            file_path=file_path,
            content_type=content_type,
            metadata=metadata,
        )
    except InvalidResponseError as err:
        # todo: add log
        print(err)
    return ret


# getfile
def get_file(object_name: str):
    minio: Minio = get_minio_client()

    try:
        ret = minio.get_object(
            bucket_name=bucket,
            object_name=object_name,
        )
    except InvalidResponseError as err:
        # todo: add log
        print(err)
        ret.close()
        ret.release_conn()
    return ret


# delete file
def delete_file(object_name: str) -> None:
    minio: Minio = get_minio_client()

    try:
        minio.remove_object(bucket_name=bucket, object_name=object_name)
    except InvalidResponseError as err:
        # todo: add log
        print(err)


# delete files
def delete_files(objects_to_delete: List) -> None:
    minio: Minio = get_minio_client()

    try:
        for del_err in minio.remove_objects(bucket, objects_to_delete):
            # todo: add log
            print("Deletion Error: {}".format(del_err))
    except InvalidResponseError as err:
        # todo: add log
        print(err)
