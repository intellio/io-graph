from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ChannelMembersNotificationRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.channelMembersNotificationRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.channelMembersNotificationRecipient")
	channelId: Optional[str] = Field(alias="channelId", default=None,)
	teamId: Optional[str] = Field(alias="teamId", default=None,)

