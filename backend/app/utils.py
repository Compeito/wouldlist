import logging
import uuid
from typing import Dict, Tuple, Any

logger = logging.getLogger('uvicorn')


def get_uuid() -> str:
    return uuid.uuid4().hex


class SerializableMixin:
    def get_serialize_fields(self) -> Tuple[str, ...]:
        raise NotImplementedError()

    def json(self) -> Dict[str, Any]:
        fields = self.get_serialize_fields()
        json = {}
        for field in fields:
            value = getattr(self, field)
            if isinstance(value, SerializableMixin):
                json[field] = value.json()
            else:
                json[field] = value
        logger.info(str(json))
        return json
