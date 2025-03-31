from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CancelPostRequest(BaseModel):
	Comment: Optional[str] = Field(alias="Comment", default=None,)

