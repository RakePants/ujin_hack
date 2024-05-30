import base64
from typing import Annotated
from fastapi import APIRouter, status, Body, Depends
from src.api.dependencies import get_s3_client
from src.services import S3Service

router = APIRouter(prefix="/s3", tags=["S3 Storage Service"])


@router.post(
    "/upload-image",
    description="Upload image to S3",
    status_code=status.HTTP_201_CREATED,
)
async def upload_image(
    b64_image: Annotated[
        str,
        Body(
            embed=False,
            example="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
        ),
    ],
    s3: Annotated[S3Service, Depends(get_s3_client)],
):
    bytes_image = base64.b64decode(b64_image)
    return await s3.upload_image(bytes_image)
