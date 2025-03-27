from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32MobileAppCatalogPackageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Win32MobileAppCatalogPackage]] = Field(alias="value", default=None,)

from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

