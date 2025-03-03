from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermStoreLocalizedDescriptionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TermStoreLocalizedDescription]] = Field(default=None,alias="value",)

from .term_store_localized_description import TermStoreLocalizedDescription

