from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintUsageByUserCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PrintUsageByUser] = Field(alias="value",)

from .print_usage_by_user import PrintUsageByUser

