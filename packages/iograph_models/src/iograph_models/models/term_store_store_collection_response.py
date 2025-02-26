from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermStoreStoreCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TermStoreStore] = Field(alias="value",)

from .term_store_store import TermStoreStore

