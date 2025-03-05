from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamCreatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	teamDescription: Optional[str] = Field(alias="teamDescription",default=None,)
	teamDisplayName: Optional[str] = Field(alias="teamDisplayName",default=None,)
	teamId: Optional[str] = Field(alias="teamId",default=None,)

from .identity_set import IdentitySet

