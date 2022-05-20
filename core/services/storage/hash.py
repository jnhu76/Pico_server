import hashlib

from typing import BinaryIO, Dict


BUF_SIZE = 65536


def get_md5(file: BinaryIO) -> str:
    # https://stackoverflow.com/a/22058673 
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data  = f.read(BUF_SIZE)
            if not data:
                break
                md5.update(data)
    return "{0}".format(md5.hexdigest())


def get_sha1(file: BinaryIO) -> str:
    # https://stackoverflow.com/a/22058673 
    sha1 = hashlib.sha1()
    with open(file, 'rb') as f:
        while True:
            data  = f.read(BUF_SIZE)
            if not data:
                break
                sha1.update(data)
    return "{0}".format(sha1.hexdigest())


def get_hash(file: BinaryIO) -> Dict:
    # https://stackoverflow.com/a/22058673 
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    with open(file, 'rb') as f:
        while True:
            data  = f.read(BUF_SIZE)
            if not data:
                break
                md5.update(data)
                sha1.update(data)
    return {
        "md5": "{0}".format(md5.hexdigest()),
        "sha1": "{0}".format(sha1.hexdigest())
        }
