from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Mark_as_not_junkPostRequest(BaseModel):
	MoveToInbox: Optional[bool] = Field(alias="MoveToInbox", default=None,)

