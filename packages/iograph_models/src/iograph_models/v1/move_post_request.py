from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MovePostRequest(BaseModel):
	DestinationId: Optional[str] = Field(alias="DestinationId", default=None,)

