from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChannelDeletedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	channelDisplayName: Optional[str] = Field(alias="channelDisplayName",default=None,)
	channelId: Optional[str] = Field(alias="channelId",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)

from .identity_set import IdentitySet

