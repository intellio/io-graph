from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DbcsPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)

