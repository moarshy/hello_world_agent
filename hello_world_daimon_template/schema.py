from pydantic import BaseModel


class InputSchema(BaseModel):
    name: str
    description: str
    param1: int
    param2: int
