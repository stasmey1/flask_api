from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int
    username: str
    email: str
