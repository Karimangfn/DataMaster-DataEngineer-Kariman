import json
import yaml
from pathlib import Path

def convert_to_json(response_text):
    """
    Converte o texto da resposta da API em JSON.
    """
    try:
        data = json.loads(response_text)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro ao converter a resposta para JSON: {e}")

def load_config(config_filename):
    ROOT_DIR = Path(__file__).resolve().parents[2]
    config_path = ROOT_DIR / config_filename

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Arquivo {config_filename} não encontrado no diretório: {ROOT_DIR}")
        raise
