from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Mark_readPostRequest(BaseModel):
	messageIds: list[Optional[str]] = Field(alias="messageIds",)


