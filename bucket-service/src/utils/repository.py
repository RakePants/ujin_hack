import uuid
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from fastapi import HTTPException, status
from aiobotocore.client import AioBaseClient
from botocore.exceptions import ClientError
from aiobotocore.session import get_session


class AbstractRepository(ABC):
    @abstractmethod
    async def get(self, *args, **kwargs):
        pass

    @abstractmethod
    async def put(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete(self, *args, **kwargs):
        pass


class S3Repository(AbstractRepository):
    access_key = None
    secret_key = None
    endpoint_url = None
    bucket_name = None

    config = {
        "aws_access_key_id": access_key,
        "aws_secret_access_key": secret_key,
        "endpoint_url": endpoint_url,
    }
    bucket_name = bucket_name
    session = get_session()

    @asynccontextmanager
    async def get_client(self) -> AioBaseClient:
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def get(self, id: str) -> str:
        try:
            async with self.get_client() as client:
                return await client.get_object(Bucket=self.bucket_name, Key=id)
        except ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e
            )

    async def put(self, file: bytes) -> uuid.UUID:
        try:
            async with self.get_client() as client:
                name = uuid.uuid4()
                await client.put_object(Body=file, Bucket=self.bucket_name, Key=name)
                return name
        except ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e
            )

    async def delete(self, name: str):
        try:
            async with self.get_client() as client:
                await client.delete_object(Bucket=self.bucket_name, Key=name)
        except ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e
            )
