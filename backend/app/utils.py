import logging
from typing import Dict, Union, Tuple, Any

logger = logging.getLogger('uvicorn')


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
