from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkApplicationIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkApplicationIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.teamworkApplicationIdentity")
	applicationIdentityType: Optional[TeamworkApplicationIdentityType | str] = Field(alias="applicationIdentityType", default=None,)

from .teamwork_application_identity_type import TeamworkApplicationIdentityType

