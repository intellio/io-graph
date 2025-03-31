from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHuntingRowResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityHuntingRowResult]] = Field(alias="value", default=None,)

from .security_hunting_row_result import SecurityHuntingRowResult
