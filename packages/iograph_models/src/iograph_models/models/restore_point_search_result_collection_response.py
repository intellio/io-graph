from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestorePointSearchResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RestorePointSearchResult] = Field(alias="value",)

from .restore_point_search_result import RestorePointSearchResult

