from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32CatalogAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Win32CatalogApp]] = Field(alias="value", default=None,)

from .win32_catalog_app import Win32CatalogApp
