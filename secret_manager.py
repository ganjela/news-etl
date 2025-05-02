from google.cloud import secretmanager

class SecretManager:
    def __init__(self):
        self.client = secretmanager.SecretManagerServiceClient()
        self.project_id = "apple-news-db6d6"

    def get_secret(self, secret_id, version_id="latest"):
        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"
        response = self.client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
