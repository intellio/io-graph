from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Unset_reactionPostRequest(BaseModel):
	reactionType: Optional[str] = Field(alias="reactionType", default=None,)

