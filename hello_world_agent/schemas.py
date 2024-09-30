from pydantic import BaseModel


class InputSchema(BaseModel):
    firstname: str
    surname: str
