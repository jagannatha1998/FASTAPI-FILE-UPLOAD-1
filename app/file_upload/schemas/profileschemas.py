from typing import Any
from pydantic import BaseModel

class ProfileResponseSchema(BaseModel):
    URL: str | None = None