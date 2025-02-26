from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHostPairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityHostPair] = Field(alias="value",)

from .security_host_pair import SecurityHostPair

