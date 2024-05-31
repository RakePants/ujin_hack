from src.infrastructure.integrations.s3.base import BaseS3
import httpx


class ServiceS3(BaseS3):
    client: httpx.AsyncClient

    async def upload_image(self, file: str) -> dict:
        res = None
        async with httpx.AsyncClient() as client:
            res = await client.post('http://localhost:8001/s3/upload-image', json=file)
        return res.json()
