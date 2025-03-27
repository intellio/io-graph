from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsQualityUpdateCatalogProductRevisionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsQualityUpdateCatalogProductRevision]] = Field(alias="value", default=None,)

from .windows_quality_update_catalog_product_revision import WindowsQualityUpdateCatalogProductRevision

