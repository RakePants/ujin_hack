import uuid
from src.repositories import S3Client


class S3Service:
    def __init__(self, client: type[S3Client]):
        self.client: S3Client = client()

    async def upload_image(self, image: bytes) -> uuid.UUID:
        return await self.client.put(image)
