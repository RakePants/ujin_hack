from src.services import S3Service
from src.repositories import S3Client


def get_s3_client():
    return S3Service(S3Client)
