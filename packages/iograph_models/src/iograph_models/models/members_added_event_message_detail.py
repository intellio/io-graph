from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MembersAddedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)
	members: list[TeamworkUserIdentity] = Field(alias="members",)
	visibleHistoryStartDateTime: Optional[datetime] = Field(default=None,alias="visibleHistoryStartDateTime",)

from .identity_set import IdentitySet
from .teamwork_user_identity import TeamworkUserIdentity

