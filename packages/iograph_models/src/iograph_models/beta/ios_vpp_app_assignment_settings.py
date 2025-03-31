from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IosVppAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.iosVppAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.iosVppAppAssignmentSettings")
	isRemovable: Optional[bool] = Field(alias="isRemovable", default=None,)
	preventAutoAppUpdate: Optional[bool] = Field(alias="preventAutoAppUpdate", default=None,)
	preventManagedAppBackup: Optional[bool] = Field(alias="preventManagedAppBackup", default=None,)
	uninstallOnDeviceRemoval: Optional[bool] = Field(alias="uninstallOnDeviceRemoval", default=None,)
	useDeviceLicensing: Optional[bool] = Field(alias="useDeviceLicensing", default=None,)
	vpnConfigurationId: Optional[str] = Field(alias="vpnConfigurationId", default=None,)

