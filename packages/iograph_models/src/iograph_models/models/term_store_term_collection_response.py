from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermStoreTermCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TermStoreTerm] = Field(alias="value",)

from .term_store_term import TermStoreTerm

