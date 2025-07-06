from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class IngestFilesCSV:
    def __init__(self, config):
        self.config = config
        self.blob_service_client = BlobServiceClient(account_url=f"https://{self.config['destination']['storage']['raw']['account']}",
                                                     credential=self.config['azure']['sas_token'])
        self.container_client = self.blob_service_client.get_container_client(self.config['destination']['storage']['raw']['container'])

    def ingest(self, source_path: str, destination_path: str):
        blob_client = self.container_client.get_blob_client(destination_path)
        
        with open(source_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Arquivo {source_path} movido para {destination_path}")

    def move_file(self, source, destination):
        self.ingest(source, destination)
