from typing import Dict, List

from pydantic import BaseModel, AnyUrl


class FirebaseToken(BaseModel):
    name: str
    picture: AnyUrl
    iss: AnyUrl
    aud: str
    auth_time: int
    user_id: str
    sub: str
    iat: int
    exp: int
    firebase: Dict[str, List[str]]
    sign_in_provider: str
    uid: str
