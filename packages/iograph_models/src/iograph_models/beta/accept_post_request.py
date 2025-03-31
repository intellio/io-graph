from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AcceptPostRequest(BaseModel):
	SendResponse: Optional[bool] = Field(alias="SendResponse", default=None,)
	Comment: Optional[str] = Field(alias="Comment", default=None,)

