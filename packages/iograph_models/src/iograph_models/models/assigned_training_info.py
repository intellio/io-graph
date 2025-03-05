from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignedTrainingInfo(BaseModel):
	assignedUserCount: Optional[int] = Field(default=None,alias="assignedUserCount",)
	completedUserCount: Optional[int] = Field(default=None,alias="completedUserCount",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


