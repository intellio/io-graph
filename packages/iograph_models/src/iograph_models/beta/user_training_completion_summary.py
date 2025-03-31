from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserTrainingCompletionSummary(BaseModel):
	completedUsersCount: Optional[int] = Field(alias="completedUsersCount", default=None,)
	inProgressUsersCount: Optional[int] = Field(alias="inProgressUsersCount", default=None,)
	notCompletedUsersCount: Optional[int] = Field(alias="notCompletedUsersCount", default=None,)
	notStartedUsersCount: Optional[int] = Field(alias="notStartedUsersCount", default=None,)
	previouslyAssignedUsersCount: Optional[int] = Field(alias="previouslyAssignedUsersCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

