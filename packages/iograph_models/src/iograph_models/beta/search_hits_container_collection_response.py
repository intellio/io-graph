from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchHitsContainerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SearchHitsContainer]] = Field(alias="value", default=None,)

from .search_hits_container import SearchHitsContainer
