from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedIOSStoreAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedIOSStoreApp]] = Field(alias="value", default=None,)

from .managed_i_o_s_store_app import ManagedIOSStoreApp
