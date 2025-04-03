from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerAssignedToTaskBoardTaskFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerAssignedToTaskBoardTaskFormat"] = Field(alias="@odata.type", default="#microsoft.graph.plannerAssignedToTaskBoardTaskFormat")
	orderHintsByAssignee: Optional[PlannerOrderHintsByAssignee] = Field(alias="orderHintsByAssignee", default=None,)
	unassignedOrderHint: Optional[str] = Field(alias="unassignedOrderHint", default=None,)

from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee
