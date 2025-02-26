from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PlannerAssignment(BaseModel):
	assignedBy: Optional[IdentitySet] = Field(default=None,alias="assignedBy",)
	assignedDateTime: Optional[datetime] = Field(default=None,alias="assignedDateTime",)
	orderHint: Optional[str] = Field(default=None,alias="orderHint",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

