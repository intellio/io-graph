from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChannelSharingUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	ownerTeamId: Optional[str] = Field(alias="ownerTeamId",default=None,)
	ownerTenantId: Optional[str] = Field(alias="ownerTenantId",default=None,)
	sharedChannelId: Optional[str] = Field(alias="sharedChannelId",default=None,)

from .identity_set import IdentitySet

