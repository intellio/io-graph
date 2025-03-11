from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppMsiInformation(BaseModel):
	packageType: Optional[Win32LobAppMsiPackageType | str] = Field(alias="packageType",default=None,)
	productCode: Optional[str] = Field(alias="productCode",default=None,)
	productName: Optional[str] = Field(alias="productName",default=None,)
	productVersion: Optional[str] = Field(alias="productVersion",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	requiresReboot: Optional[bool] = Field(alias="requiresReboot",default=None,)
	upgradeCode: Optional[str] = Field(alias="upgradeCode",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .win32_lob_app_msi_package_type import Win32LobAppMsiPackageType

