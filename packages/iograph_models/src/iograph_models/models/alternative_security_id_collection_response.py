from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlternativeSecurityIdCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AlternativeSecurityId] = Field(alias="value",)

from .alternative_security_id import AlternativeSecurityId

