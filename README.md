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

## todo

1. 设计cache

2. 利用gRPC优化api

3. 添加图片 tag

## 继续阅读

1. Facebook Heystack 设计

   https://www.scaleyourapp.com/facebook-photo-storage-architecture/

   paper：Finding a needle in Haystack: Facebook’s photo storage

   视频： https://www.coursera.org/lecture/cloud-sys-software/facebook-haystack-based-design-Zay9r

2. f4: Facebook’s Warm BLOB Storage System

3. [Imgix](https://imgix.com/) - Powerful Image
Processing, Simple APIs

   - API https://docs.imgix.com/apis/management

   - Library https://docs.imgix.com/libraries

   - Best-practices https://docs.imgix.com/best-practices

## 参考文档

1. https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework

2. https://tortoise-orm.readthedocs.io/en/latest/

3. https://docs.wand-py.org/en/0.6.7/

4. https://fastapi.tiangolo.com/

8. https://github.com/nsidnev/fastapi-realworld-example-app

9. https://stackoverflow.com/questions/65716897/testing-in-fastapi-using-tortoise-orm

10. https://segmentfault.com/a/1190000041855999