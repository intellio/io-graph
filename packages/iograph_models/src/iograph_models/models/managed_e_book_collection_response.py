from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedEBookCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedEBook] = Field(alias="value",)

from .managed_e_book import ManagedEBook

