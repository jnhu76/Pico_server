# Pico_server


## 项目文档

项目结构参考 [What are the best practices for structuring a FastAPI project?](https://stackoverflow.com/a/64987404)

minio 返回信息：

```sh
{
  "filename": "IMG_0006.JPG",
  "ret": {
    "_bucket_name": "pico",
    "_object_name": "IMG_0006.JPG",
    "_version_id": null,
    "_etag": "a09b2771acb3f2eee01f6ff0204668f0",
    "_http_headers": {
      "Accept-Ranges": "bytes",
      "Content-Length": "0",
      "Content-Security-Policy": "block-all-mixed-content",
      "ETag": "\"a09b2771acb3f2eee01f6ff0204668f0\"",
      "Server": "MinIO",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Vary": "Origin, Accept-Encoding",
      "X-Amz-Request-Id": "16F11CE02AAD7DCB",
      "X-Content-Type-Options": "nosniff",
      "X-Xss-Protection": "1; mode=block",
      "Date": "Sat, 21 May 2022 11:58:07 GMT"
    },
    "_last_modified": null,
    "_location": null
  }
}
```

### 参考文档

1. https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework

2. https://tortoise-orm.readthedocs.io/en/latest/

3. https://docs.wand-py.org/en/0.6.7/

4. https://fastapi.tiangolo.com/

5. https://github.com/hhatto/autopep8#pyproject-toml

6. https://github.com/ni/python-styleguide/blob/main/pyproject.toml

7. https://mypy.readthedocs.io/en/stable/config_file.html#using-a-pyproject-toml-file

8. https://github.com/nsidnev/fastapi-realworld-example-app

9. https://github.com/tiangolo/fastapi/issues/529