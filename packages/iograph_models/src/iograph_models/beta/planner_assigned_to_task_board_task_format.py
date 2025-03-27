from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerAssignedToTaskBoardTaskFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	orderHintsByAssignee: Optional[PlannerOrderHintsByAssignee] = Field(alias="orderHintsByAssignee", default=None,)
	unassignedOrderHint: Optional[str] = Field(alias="unassignedOrderHint", default=None,)

from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

