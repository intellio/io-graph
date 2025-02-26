from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamCreatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)
	teamDescription: Optional[str] = Field(default=None,alias="teamDescription",)
	teamDisplayName: Optional[str] = Field(default=None,alias="teamDisplayName",)
	teamId: Optional[str] = Field(default=None,alias="teamId",)

from .identity_set import IdentitySet

