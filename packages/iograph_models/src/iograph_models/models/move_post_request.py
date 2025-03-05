from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MovePostRequest(BaseModel):
	DestinationId: Optional[str] = Field(default=None,alias="DestinationId",)


