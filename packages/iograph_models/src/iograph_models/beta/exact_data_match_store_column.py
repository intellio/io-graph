from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExactDataMatchStoreColumn(BaseModel):
	ignoredDelimiters: Optional[list[str]] = Field(alias="ignoredDelimiters", default=None,)
	isCaseInsensitive: Optional[bool] = Field(alias="isCaseInsensitive", default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

