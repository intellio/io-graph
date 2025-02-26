from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosStoreAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isRemovable: Optional[bool] = Field(default=None,alias="isRemovable",)
	uninstallOnDeviceRemoval: Optional[bool] = Field(default=None,alias="uninstallOnDeviceRemoval",)
	vpnConfigurationId: Optional[str] = Field(default=None,alias="vpnConfigurationId",)


