from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
	queryString: Optional[str] = Field(alias="queryString", default=None,)
	queryTemplate: Optional[str] = Field(alias="queryTemplate", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

