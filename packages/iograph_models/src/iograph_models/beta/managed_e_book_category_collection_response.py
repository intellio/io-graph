from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedEBookCategoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedEBookCategory]] = Field(alias="value", default=None,)

from .managed_e_book_category import ManagedEBookCategory
