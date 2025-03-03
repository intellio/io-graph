from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OptionalClaimCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OptionalClaim]] = Field(default=None,alias="value",)

from .optional_claim import OptionalClaim

