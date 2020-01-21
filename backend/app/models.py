from typing import Tuple

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from .utils import get_uuid, SerializableMixin
from .db import Base


class User(SerializableMixin, Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String)
    screen_name = Column(String)
    photo_url = Column(String)

    items = relationship('Item', back_populates='user')

    def get_serialize_fields(self) -> Tuple[str, ...]:
        return 'name', 'photo_url', 'screen_name', 'items'

    def __str__(self) -> str:
        return f'{self.name}(@{self.screen_name})'


class Item(SerializableMixin, Base):
    __tablename__ = 'items'

    uid = Column(String, primary_key=True, index=True, default=get_uuid)
    text = Column(String)

    user_id = Column(String, ForeignKey('users.uid'))
    user = relationship('User', back_populates='items')

    def get_serialize_fields(self) -> Tuple[str, ...]:
        return 'user', 'text'
