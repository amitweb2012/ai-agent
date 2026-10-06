from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "http://localhost:11434/v1")
    api_key: str = os.getenv("API_KEY", "ollama")
    model: str = os.getenv("MODEL", "qwen3:1.7b")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
    rag_min_similarity: float = float(os.getenv("RAG_MIN_SIMILARITY", "0.5"))


settings = Settings()
