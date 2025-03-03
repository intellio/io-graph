from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignedLabelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AssignedLabel]] = Field(default=None,alias="value",)

from .assigned_label import AssignedLabel

