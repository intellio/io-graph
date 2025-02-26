from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ChatViewpoint(BaseModel):
	isHidden: Optional[bool] = Field(default=None,alias="isHidden",)
	lastMessageReadDateTime: Optional[datetime] = Field(default=None,alias="lastMessageReadDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


