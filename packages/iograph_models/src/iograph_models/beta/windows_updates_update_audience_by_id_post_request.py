from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows_updates_update_audience_by_idPostRequest(BaseModel):
	memberEntityType: Optional[str] = Field(alias="memberEntityType", default=None,)
	addMembers: Optional[list[str]] = Field(alias="addMembers", default=None,)
	removeMembers: Optional[list[str]] = Field(alias="removeMembers", default=None,)
	addExclusions: Optional[list[str]] = Field(alias="addExclusions", default=None,)
	removeExclusions: Optional[list[str]] = Field(alias="removeExclusions", default=None,)

