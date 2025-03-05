from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChannelUnsetAsFavoriteByDefaultEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	channelId: Optional[str] = Field(default=None,alias="channelId",)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="initiator",)

from .identity_set import IdentitySet

