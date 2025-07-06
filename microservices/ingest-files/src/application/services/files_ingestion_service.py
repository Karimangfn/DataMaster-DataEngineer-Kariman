import os

from src.domain.exceptions.exceptions import (InvalidSourcePathError,
                                              NotFoundError,
                                              UnsupportedFileTypeError)
from src.infrastructure.config.strategy_registry import \
    FILE_INGESTION_STRATEGIES


class IngestionService:
    """
    Service responsible for managing file ingestion based on file extension.
    """

    def __init__(self, config: dict):
        """
        Initialize the ingestion service with the provided configuration.

        Args:
            config (dict): Dictionary containing source and destination config.

        Raises:
            InvalidSourcePathError: If 'source.folder' is missing.
            NotFoundError: If no files are found in the source directory.
            UnsupportedFileTypeError: If the detected file extension is
            unsupported.
        """
        self.config = config
        self.source_path = self.config.get("source", {}).get("folder", "")

        if not isinstance(self.source_path, str):
            raise InvalidSourcePathError(
                f"The field 'source.folder' must be a string. "
                f"Received: {self.source_path}"
            )

        if not self.source_path or not os.path.isdir(self.source_path):
            raise InvalidSourcePathError(
                f"Invalid or non-existent source path: {self.source_path}"
            )

        self.strategy = self._get_strategy()

    def _get_strategy(self):
        """
        Detects the file type in the source folder and selects
        the appropriate ingestion strategy.

        Returns:
            An instance of a class implementing the corresponding ingestion
            strategy.

        Raises:
            ValueError: If no files are found or if the file type is
                unsupported.
        """
        files = [
            f for f in os.listdir(self.source_path)
            if os.path.isfile(os.path.join(self.source_path, f))
        ]
        if not files:
            raise NotFoundError(
                "No files found in the source folder."
            )

        file_extension = self._get_file_extension(files[0])
        if file_extension not in FILE_INGESTION_STRATEGIES:
            raise UnsupportedFileTypeError(
                f"Ingestion for file type '{file_extension}' is not supported."
            )

        StrategyClass = FILE_INGESTION_STRATEGIES[file_extension]
        return StrategyClass(self.config)

    def _get_file_extension(self, filename: str) -> str:
        """
        Extracts the file extension from a given filename.

        Args:
            filename (str): Name of the file.

        Returns:
            str: Lowercase file extension (e.g., 'csv').
        """
        _, extension = os.path.splitext(filename)
        return extension[1:].lower()

    def execute(self) -> None:
        """
        Executes the ingestion process for all files found
        in the source folder.
        """
        files = os.listdir(self.source_path)
        container = self.config["destination"]["storage"]["raw"]["container"]
        destination_prefix = f"{container}/"

        for file in files:
            full_source_path = os.path.join(self.source_path, file)
            destination_path = os.path.join(destination_prefix, file)
            self.strategy.ingest(full_source_path, destination_path)
