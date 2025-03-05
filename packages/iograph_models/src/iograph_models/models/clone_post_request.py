from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClonePostRequest(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	description: Optional[str] = Field(default=None,alias="description",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	classification: Optional[str] = Field(default=None,alias="classification",)
	visibility: Optional[TeamVisibilityType] = Field(default=None,alias="visibility",)
	partsToClone: Optional[ClonableTeamParts] = Field(default=None,alias="partsToClone",)

from .team_visibility_type import TeamVisibilityType
from .clonable_team_parts import ClonableTeamParts

