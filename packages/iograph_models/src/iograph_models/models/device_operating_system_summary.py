from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceOperatingSystemSummary(BaseModel):
	androidCorporateWorkProfileCount: Optional[int] = Field(default=None,alias="androidCorporateWorkProfileCount",)
	androidCount: Optional[int] = Field(default=None,alias="androidCount",)
	androidDedicatedCount: Optional[int] = Field(default=None,alias="androidDedicatedCount",)
	androidDeviceAdminCount: Optional[int] = Field(default=None,alias="androidDeviceAdminCount",)
	androidFullyManagedCount: Optional[int] = Field(default=None,alias="androidFullyManagedCount",)
	androidWorkProfileCount: Optional[int] = Field(default=None,alias="androidWorkProfileCount",)
	configMgrDeviceCount: Optional[int] = Field(default=None,alias="configMgrDeviceCount",)
	iosCount: Optional[int] = Field(default=None,alias="iosCount",)
	macOSCount: Optional[int] = Field(default=None,alias="macOSCount",)
	unknownCount: Optional[int] = Field(default=None,alias="unknownCount",)
	windowsCount: Optional[int] = Field(default=None,alias="windowsCount",)
	windowsMobileCount: Optional[int] = Field(default=None,alias="windowsMobileCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


