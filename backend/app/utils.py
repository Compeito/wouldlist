import logging
import uuid
from typing import Dict, Tuple, Any

logger = logging.getLogger('uvicorn')


def get_uuid() -> str:
    return uuid.uuid4().hex


class SerializableMixin:
    def get_serialize_fields(self) -> Tuple[str, ...]:
        raise NotImplementedError()

    @staticmethod
    def _to_camel_case(snake_case_str: str) -> str:
        s = snake_case_str.split('_')
        return s[0] + ''.join(x.title() for x in s[1:])

    def json(self, fields_extra: Tuple[str, ...] = ()) -> Dict[str, Any]:
        fields = self.get_serialize_fields() + fields_extra
        json = {}
        for field in fields:
            value = getattr(self, field)
            key = self._to_camel_case(field)
            if isinstance(value, SerializableMixin):
                json[key] = value.json()
            else:
                json[key] = value
        logger.info(str(json))
        return json
