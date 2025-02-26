from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityDataSourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityDataSource] = Field(alias="value",)

from .security_data_source import SecurityDataSource

