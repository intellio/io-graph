from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityUserSourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityUserSource] = Field(alias="value",)

from .security_user_source import SecurityUserSource

