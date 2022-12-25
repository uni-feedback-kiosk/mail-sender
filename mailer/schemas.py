from pydantic import BaseModel


class EmailData(BaseModel):
    subject: str
    body: str
