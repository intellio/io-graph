from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClonePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname", default=None,)
	classification: Optional[str] = Field(alias="classification", default=None,)
	visibility: Optional[TeamVisibilityType | str] = Field(alias="visibility", default=None,)
	partsToClone: Optional[ClonableTeamParts | str] = Field(alias="partsToClone", default=None,)

from .team_visibility_type import TeamVisibilityType
from .clonable_team_parts import ClonableTeamParts

