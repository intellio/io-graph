from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePointSearchResponse(BaseModel):
	noResultProtectionUnitIds: Optional[list[str]] = Field(alias="noResultProtectionUnitIds",default=None,)
	searchResponseId: Optional[str] = Field(alias="searchResponseId",default=None,)
	searchResults: Optional[list[RestorePointSearchResult]] = Field(alias="searchResults",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .restore_point_search_result import RestorePointSearchResult

