from pydantic import BaseModel


class TaskPayload(BaseModel):
    task: str
    apikey: str
    answer: str | list[str]


class TaskResponse(BaseModel):
    code: int
    message: str
