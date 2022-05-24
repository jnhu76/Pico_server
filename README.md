# Pico_server


## 项目文档

### V1-API

1. `GET` `/api/v1/info/{checksum}`

   Get Image Informaction.

2. `GET` `/api/v1/file/{checksum}`

   Get Image file.

   功能：

   - Resize

   - Corp

   - Sample

   - Blur

   - Gaussian Blur

   - Motion Blur

   - Rotational Blur

   - Sharpen

   - Flip / Flop

   - Rotate

   - Format

   - Quality

3. `POST` `/api/v1/info/{checksum}`

   Upload Image file.


### 参考文档

1. https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework

2. https://tortoise-orm.readthedocs.io/en/latest/

3. https://docs.wand-py.org/en/0.6.7/

4. https://fastapi.tiangolo.com/

8. https://github.com/nsidnev/fastapi-realworld-example-app

9. https://stackoverflow.com/questions/65716897/testing-in-fastapi-using-tortoise-orm