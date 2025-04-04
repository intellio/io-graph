from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CopyPostRequest(BaseModel):
	DestinationId: Optional[str] = Field(alias="DestinationId", default=None,)

