from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FavoritePostRequest(BaseModel):
	messageIds: Optional[list[str]] = Field(alias="messageIds", default=None,)

