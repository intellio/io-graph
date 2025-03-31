from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_requestPostRequest(BaseModel):
	decision: Optional[str] = Field(alias="decision", default=None,)
	assignmentState: Optional[str] = Field(alias="assignmentState", default=None,)
	schedule: Optional[GovernanceSchedule] = Field(alias="schedule", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)

from .governance_schedule import GovernanceSchedule
