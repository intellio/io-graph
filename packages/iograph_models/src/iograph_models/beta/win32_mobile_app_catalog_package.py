from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Win32MobileAppCatalogPackage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.win32MobileAppCatalogPackage"] = Field(alias="@odata.type", default="#microsoft.graph.win32MobileAppCatalogPackage")
	productDisplayName: Optional[str] = Field(alias="productDisplayName", default=None,)
	productId: Optional[str] = Field(alias="productId", default=None,)
	publisherDisplayName: Optional[str] = Field(alias="publisherDisplayName", default=None,)
	versionDisplayName: Optional[str] = Field(alias="versionDisplayName", default=None,)
	applicableArchitectures: Optional[WindowsArchitecture | str] = Field(alias="applicableArchitectures", default=None,)
	branchDisplayName: Optional[str] = Field(alias="branchDisplayName", default=None,)
	locales: Optional[list[str]] = Field(alias="locales", default=None,)
	packageAutoUpdateCapable: Optional[bool] = Field(alias="packageAutoUpdateCapable", default=None,)

from .windows_architecture import WindowsArchitecture

