from google.cloud import storage


class GCStorage:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket_name= 'correlation-one-371005.appspot.com'

    def upload_file(self,file):
        bucket=self.storage_client.get_bucket(self.bucket_name)
        file_path=file.filename
        bolb=bucket.blob(file_path)
        bolb.upload_from_file(file.file, content_type='image/jpeg')
        return f'https://storage.cloud.google.com/{self.bucket_name}/{file_path}'
