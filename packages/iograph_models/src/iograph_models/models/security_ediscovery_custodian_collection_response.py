from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEdiscoveryCustodianCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityEdiscoveryCustodian] = Field(alias="value",)

from .security_ediscovery_custodian import SecurityEdiscoveryCustodian

