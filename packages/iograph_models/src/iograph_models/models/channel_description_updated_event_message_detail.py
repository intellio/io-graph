from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChannelDescriptionUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	channelDescription: Optional[str] = Field(default=None,alias="channelDescription",)
	channelId: Optional[str] = Field(default=None,alias="channelId",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)

from .identity_set import IdentitySet

