from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Mark_unreadPostRequest(BaseModel):
	messageIds: list[Optional[str]] = Field(alias="messageIds",)


