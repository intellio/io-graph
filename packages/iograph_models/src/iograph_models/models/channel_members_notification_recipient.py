from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChannelMembersNotificationRecipient(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	channelId: Optional[str] = Field(default=None,alias="channelId",)
	teamId: Optional[str] = Field(default=None,alias="teamId",)


