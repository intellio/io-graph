from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkApplicationIdentity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationIdentityType: Optional[TeamworkApplicationIdentityType] = Field(default=None,alias="applicationIdentityType",)

from .teamwork_application_identity_type import TeamworkApplicationIdentityType

