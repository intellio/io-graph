from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Move_to_catalogPostRequest(BaseModel):
	catalogId: Optional[str] = Field(alias="catalogId", default=None,)

