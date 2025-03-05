from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamDescriptionUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="initiator",)
	teamDescription: Optional[str] = Field(default=None,alias="teamDescription",)
	teamId: Optional[str] = Field(default=None,alias="teamId",)

from .identity_set import IdentitySet

