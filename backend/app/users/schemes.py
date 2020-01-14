from typing import Dict, List

from pydantic import BaseModel, AnyUrl


class FirebaseIdentities(BaseModel):
    identities: Dict[str, List[str]]
    sign_in_provider: str


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
    firebase: FirebaseIdentities
    uid: str
