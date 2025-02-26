from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AcceptPostRequest(BaseModel):
	SendResponse: Optional[bool] = Field(default=None,alias="SendResponse",)
	Comment: Optional[str] = Field(default=None,alias="Comment",)


