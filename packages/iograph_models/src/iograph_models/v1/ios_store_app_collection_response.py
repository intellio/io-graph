from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosStoreAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosStoreApp]] = Field(alias="value", default=None,)

from .ios_store_app import IosStoreApp
