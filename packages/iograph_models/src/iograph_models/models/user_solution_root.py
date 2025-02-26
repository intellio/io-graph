from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserSolutionRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	workingTimeSchedule: Optional[WorkingTimeSchedule] = Field(default=None,alias="workingTimeSchedule",)

from .working_time_schedule import WorkingTimeSchedule

