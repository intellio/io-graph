from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerAssignedToTaskBoardTaskFormat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	orderHintsByAssignee: Optional[PlannerOrderHintsByAssignee] = Field(default=None,alias="orderHintsByAssignee",)
	unassignedOrderHint: Optional[str] = Field(default=None,alias="unassignedOrderHint",)

from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

