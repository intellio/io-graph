from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PayloadCompatibleAssignmentFilterCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PayloadCompatibleAssignmentFilter]] = Field(alias="value", default=None,)

from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
