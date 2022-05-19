from typing import IO, Dict, List
from minio import Minio
from minio.error import InvalidResponseError

from core.settings.app import AppSettings


bucket = AppSettings.minio_bucket

# create minio client
def get_minio_client(settings: AppSettings) -> Minio:
    minio = Minio(
        settings.minio_endpoint,
        access_key=settings.minio_access_key,
        secret_key=settings.minio_secret_key,
    )
    return minio


# upload file
def upload_file(object_name: str, file_path: str, content_type: str, metadata: Dict = {}) -> str:
    minio: Minio = get_minio_client()

    try:
        ret = minio.fput_object(
            bucket_name=bucket,
            object_name=object_name,
            file_path=file_path,
            content_type=content_type,
            metadata=metadata
        )
    except InvalidResponseError as err:
        # todo: add log
        print(err)
    return ret

# getfile
def get_file(object_name: str, file_path: str, request_headers: Dict = {}) -> Dict:
    minio: Minio = get_minio_client()

    try:
        ret = minio.fget_object(
            bucket_name=bucket,
            object_name=object_name,
            file_path=file_path,
            request_headers=request_headers
        )
    except InvalidResponseError as err:
        # todo: add log
        print(err)
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
def delete_files(objects_to_delete : List) -> None:
    minio: Minio = get_minio_client()

    try:
        for del_err in minio.remove_objects(bucket, objects_to_delete):
            # todo: add log
            print("Deletion Error: {}".format(del_err))
    except InvalidResponseError as err:
        # todo: add log
        print(err)

