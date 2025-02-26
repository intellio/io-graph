from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosVppEBookCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosVppEBook] = Field(alias="value",)

from .ios_vpp_e_book import IosVppEBook

