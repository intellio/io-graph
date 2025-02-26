from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_orderPostRequest(BaseModel):
	newAssignmentOrder: Optional[AssignmentOrder] = Field(default=None,alias="newAssignmentOrder",)

from .assignment_order import AssignmentOrder

