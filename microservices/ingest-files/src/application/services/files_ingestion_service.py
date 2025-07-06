import os
from src.strategy.ingest_files import IngestFiles

class IngestionService:
    """Gerenciador de ingestão de arquivos"""

    def __init__(self, config: dict):
        # Cria a instância de ingestão, passando a configuração
        self.ingest_files = IngestFiles(config)

    def execute(self):
        """Executa o processo de ingestão de arquivos"""
        source_path = self.ingest_files.config["source"]["folder"]
        
        # Verificando o caminho do destino correto
        # Acessando account e container para formar o destino
        account = self.ingest_files.config["destination"]["storage"]["raw"]["account"]
        container = self.ingest_files.config["destination"]["storage"]["raw"]["container"]
        
        # Combinando account e container para formar o path completo
        destination_path = f"https://{account}/{container}/"

        if not destination_path:
            raise ValueError("Caminho de destino não especificado corretamente no arquivo de configuração.")
        
        files = os.listdir(source_path)
        
        for file in files:
            full_source_path = os.path.join(source_path, file)
            full_destination_path = os.path.join(destination_path, file)
            
            self.ingest_files.ingest(full_source_path, full_destination_path)
            print(f"Arquivo {file} movido para {full_destination_path}")