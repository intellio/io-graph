from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestorePointSearchResponse(BaseModel):
	noResultProtectionUnitIds: Optional[list[str]] = Field(default=None,alias="noResultProtectionUnitIds",)
	searchResponseId: Optional[str] = Field(default=None,alias="searchResponseId",)
	searchResults: Optional[list[RestorePointSearchResult]] = Field(default=None,alias="searchResults",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .restore_point_search_result import RestorePointSearchResult

