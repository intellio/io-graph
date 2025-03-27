from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerAssignedToTaskBoardTaskFormatCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PlannerAssignedToTaskBoardTaskFormat]] = Field(alias="value", default=None,)

from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat

