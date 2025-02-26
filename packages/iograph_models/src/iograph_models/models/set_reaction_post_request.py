from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_reactionPostRequest(BaseModel):
	reactionType: Optional[str] = Field(default=None,alias="reactionType",)


