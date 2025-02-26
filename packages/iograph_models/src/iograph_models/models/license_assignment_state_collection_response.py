from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LicenseAssignmentStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[LicenseAssignmentState] = Field(alias="value",)

from .license_assignment_state import LicenseAssignmentState

