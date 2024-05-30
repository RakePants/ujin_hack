from src.utils.repository import S3Repository
from src.config import settings


class S3Client(S3Repository):
    access_key: str = settings.access_key
    secret_key: str = settings.secret_key
    endpoint_url: str = settings.endpoint_url
    bucket_name: str = settings.bucket_name
