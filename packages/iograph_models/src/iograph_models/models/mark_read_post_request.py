from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Mark_readPostRequest(BaseModel):
	messageIds: Optional[list[str]] = Field(default=None,alias="messageIds",)


