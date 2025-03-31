from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignedTrainingInfo(BaseModel):
	assignedUserCount: Optional[int] = Field(alias="assignedUserCount", default=None,)
	completedUserCount: Optional[int] = Field(alias="completedUserCount", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

