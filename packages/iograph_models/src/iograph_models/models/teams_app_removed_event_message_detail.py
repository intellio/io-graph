from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppRemovedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)
	teamsAppDisplayName: Optional[str] = Field(default=None,alias="teamsAppDisplayName",)
	teamsAppId: Optional[str] = Field(default=None,alias="teamsAppId",)

from .identity_set import IdentitySet

