import firebase_admin
from firebase_admin import storage


def initialize_app(cred):
    return firebase_admin.initialize_app(cred)


def get_bucket_path(bucket_name: str) -> str:
    bucket = storage.bucket(bucket_name)
    return bucket.path


if __name__ == "__main__":
    get_bucket_path("hey")
