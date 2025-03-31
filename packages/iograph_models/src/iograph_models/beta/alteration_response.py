from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlterationResponse(BaseModel):
	originalQueryString: Optional[str] = Field(alias="originalQueryString", default=None,)
	queryAlteration: Optional[SearchAlteration] = Field(alias="queryAlteration", default=None,)
	queryAlterationType: Optional[SearchAlterationType | str] = Field(alias="queryAlterationType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .search_alteration import SearchAlteration
from .search_alteration_type import SearchAlterationType
