from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserSolutionRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userSolutionRoot"] = Field(alias="@odata.type", default="#microsoft.graph.userSolutionRoot")
	workingTimeSchedule: Optional[WorkingTimeSchedule] = Field(alias="workingTimeSchedule", default=None,)

from .working_time_schedule import WorkingTimeSchedule
