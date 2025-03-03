from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeletedTeam(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	channels: Optional[list[Channel]] = Field(default=None,alias="channels",)

from .channel import Channel

