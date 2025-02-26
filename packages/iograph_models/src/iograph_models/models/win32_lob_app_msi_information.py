from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppMsiInformation(BaseModel):
	packageType: Optional[Win32LobAppMsiPackageType] = Field(default=None,alias="packageType",)
	productCode: Optional[str] = Field(default=None,alias="productCode",)
	productName: Optional[str] = Field(default=None,alias="productName",)
	productVersion: Optional[str] = Field(default=None,alias="productVersion",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	requiresReboot: Optional[bool] = Field(default=None,alias="requiresReboot",)
	upgradeCode: Optional[str] = Field(default=None,alias="upgradeCode",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .win32_lob_app_msi_package_type import Win32LobAppMsiPackageType

