from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftStoreForBusinessAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MicrosoftStoreForBusinessApp] = Field(alias="value",)

from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp

