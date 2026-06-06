import os


def _env_bool(name: str, default: bool) -> bool:
	value = os.getenv(name)
	if value is None:
		return default
	return value.strip().lower() in {"1", "true", "yes", "on"}

VECTOR_SIZE = 768
MAX_LINES_PER_CHUNK = 400
MAX_TOKENS = 512
EMBED_BATCH_SIZE = int(os.getenv("EMBED_BATCH_SIZE", "32"))
EMBED_MAX_RETRIES = int(os.getenv("EMBED_MAX_RETRIES", "10"))
EMBED_RETRY_DELAY = float(os.getenv("EMBED_RETRY_DELAY", "10"))

COLLECTION_NAME = os.getenv("VECTOR_COLLECTION", "pdf-books-vectors")
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
QDRANT_TIMEOUT_SECONDS = float(os.getenv("QDRANT_TIMEOUT_SECONDS", "120"))
QDRANT_UPSERT_MAX_RETRIES = int(os.getenv("QDRANT_UPSERT_MAX_RETRIES", "4"))
QDRANT_UPSERT_RETRY_DELAY = float(os.getenv("QDRANT_UPSERT_RETRY_DELAY", "2"))
QDRANT_ENSURE_PAYLOAD_INDEXES = _env_bool("QDRANT_ENSURE_PAYLOAD_INDEXES", True)
QDRANT_INDEX_FIELDS = os.getenv(
	"QDRANT_INDEX_FIELDS",
	"branch,service,repository,deployment_scope,chunk_type,symbol_name,file_path,namespace,fqn,language",
)
QDRANT_SEARCH_HNSW_EF = int(os.getenv("QDRANT_SEARCH_HNSW_EF", "128"))
QDRANT_SEARCH_EXACT = _env_bool("QDRANT_SEARCH_EXACT", False)
EMBED_URL = os.getenv("EMBED_URL", "http://embed:6667")
TOKENIZER_NAME = os.getenv("MODEL_NAME", "microsoft/codebert-base")
MODEL_NAME = os.getenv("MODEL_NAME", "microsoft/codebert-base")

QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))