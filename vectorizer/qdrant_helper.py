from qdrant_client import QdrantClient
from qdrant_client.http.exceptions import ResponseHandlingException
from qdrant_client.http.models import (
    Distance,
    VectorParams,
    Filter,
    FieldCondition,
    MatchValue,
    MatchAny,
    PointStruct,
    PayloadSchemaType,
    SearchParams,
)

def get_client(url: str = QDRANT_URL) -> QdrantClient:
    _log_tuning_once(url)
    return QdrantClient(url=url, timeout=QDRANT_TIMEOUT_SECONDS)