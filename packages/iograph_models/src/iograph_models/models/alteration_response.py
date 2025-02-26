from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlterationResponse(BaseModel):
	originalQueryString: Optional[str] = Field(default=None,alias="originalQueryString",)
	queryAlteration: Optional[SearchAlteration] = Field(default=None,alias="queryAlteration",)
	queryAlterationType: Optional[SearchAlterationType] = Field(default=None,alias="queryAlterationType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_alteration import SearchAlteration
from .search_alteration_type import SearchAlterationType

