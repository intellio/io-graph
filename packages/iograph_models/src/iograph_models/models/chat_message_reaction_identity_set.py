from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatMessageReactionIdentitySet(BaseModel):
	application: Optional[Identity] = Field(default=None,alias="application",)
	device: Optional[Identity] = Field(default=None,alias="device",)
	user: Optional[Identity] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity import Identity
from .identity import Identity
from .identity import Identity

