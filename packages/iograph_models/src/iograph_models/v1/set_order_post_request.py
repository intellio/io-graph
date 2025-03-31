from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_orderPostRequest(BaseModel):
	newAssignmentOrder: Optional[AssignmentOrder] = Field(alias="newAssignmentOrder", default=None,)

from .assignment_order import AssignmentOrder
