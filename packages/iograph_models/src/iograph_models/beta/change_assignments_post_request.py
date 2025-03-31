from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Change_assignmentsPostRequest(BaseModel):
	deviceAssignmentItems: Optional[list[DeviceAssignmentItem]] = Field(alias="deviceAssignmentItems", default=None,)

from .device_assignment_item import DeviceAssignmentItem
