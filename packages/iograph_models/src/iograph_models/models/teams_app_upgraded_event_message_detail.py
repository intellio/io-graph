from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppUpgradedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	teamsAppDisplayName: Optional[str] = Field(alias="teamsAppDisplayName",default=None,)
	teamsAppId: Optional[str] = Field(alias="teamsAppId",default=None,)

from .identity_set import IdentitySet

