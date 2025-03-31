from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RejectPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)

