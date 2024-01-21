import firebase_admin
from firebase_admin import storage


class FirebaseAdminClient:
    def __init__(self, creds: str):
        self.__initialize_app(creds)

    def __initialize_app(self, cred):
        return firebase_admin.initialize_app(cred)

    def get_bucket_path(self, bucket_name: str) -> str:
        bucket = storage.bucket(bucket_name)
        return bucket.path


if __name__ == "__main__":
    client = FirebaseAdminClient("some/path")
    client.get_bucket_path("...")
