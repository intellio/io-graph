from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHuntingRowResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityHuntingRowResult] = Field(alias="value",)

from .security_hunting_row_result import SecurityHuntingRowResult

