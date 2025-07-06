import logging
import os

from .ingest_files_csv import IngestFilesCSV


class IngestFiles:
    def __init__(self, config):
        self.config = config
        self.source_path = self.config.get("source", {}).get("folder", "")
        
        if not isinstance(self.source_path, str):
            raise ValueError(f"O campo 'source.folder' deve ser uma string. Valor recebido: {self.source_path}")

        if not self.source_path or not os.path.isdir(self.source_path):
            raise ValueError(f"Caminho de origem inválido ou não encontrado: {self.source_path}")
        
        self.strategy = self._get_strategy()

    _INGESTIONTYPES = {
        "csv": IngestFilesCSV,
    }

    def _get_strategy(self):
        files = [f for f in os.listdir(self.source_path) if os.path.isfile(os.path.join(self.source_path, f))]
        
        if not files:
            raise ValueError("Nenhum arquivo encontrado na pasta de origem.")

        file_extension = self._get_file_extension(files[0]) 
        logging.info(f"Extensão do arquivo encontrado: {file_extension}")

        if file_extension not in self._INGESTIONTYPES:
            raise ValueError(f"Ingestão para o tipo de arquivo '{file_extension}' não suportada.")
        
        return self._INGESTIONTYPES[file_extension](self.config)

    def _get_file_extension(self, filename: str):
        _, extension = os.path.splitext(filename)
        return extension[1:].lower()

    def ingest(self, source_path: str, destination_path: str):
        return self.strategy.ingest(source_path, destination_path)
