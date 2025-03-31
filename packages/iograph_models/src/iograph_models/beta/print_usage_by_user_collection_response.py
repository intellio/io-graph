from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintUsageByUserCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PrintUsageByUser]] = Field(alias="value", default=None,)

from .print_usage_by_user import PrintUsageByUser
