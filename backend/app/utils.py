import logging
from typing import Dict, Union, Tuple

logger = logging.getLogger('uvicorn')


class SerializableMixin:
    def get_serialize_fields(self) -> Tuple[str, ...]:
        raise NotImplementedError()

    def json(self) -> Dict[str, Union[str, int]]:
        fields = self.get_serialize_fields()
        json = {}
        for field in fields:
            value: Union[str, int] = getattr(self, field)
            json[field] = value
        logger.info(str(json))
        return json
