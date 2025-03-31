from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceOperatingSystemSummary(BaseModel):
	androidCorporateWorkProfileCount: Optional[int] = Field(alias="androidCorporateWorkProfileCount", default=None,)
	androidCount: Optional[int] = Field(alias="androidCount", default=None,)
	androidDedicatedCount: Optional[int] = Field(alias="androidDedicatedCount", default=None,)
	androidDeviceAdminCount: Optional[int] = Field(alias="androidDeviceAdminCount", default=None,)
	androidFullyManagedCount: Optional[int] = Field(alias="androidFullyManagedCount", default=None,)
	androidWorkProfileCount: Optional[int] = Field(alias="androidWorkProfileCount", default=None,)
	aospUserAssociatedCount: Optional[int] = Field(alias="aospUserAssociatedCount", default=None,)
	aospUserlessCount: Optional[int] = Field(alias="aospUserlessCount", default=None,)
	chromeOSCount: Optional[int] = Field(alias="chromeOSCount", default=None,)
	configMgrDeviceCount: Optional[int] = Field(alias="configMgrDeviceCount", default=None,)
	iosCount: Optional[int] = Field(alias="iosCount", default=None,)
	linuxCount: Optional[int] = Field(alias="linuxCount", default=None,)
	macOSCount: Optional[int] = Field(alias="macOSCount", default=None,)
	unknownCount: Optional[int] = Field(alias="unknownCount", default=None,)
	windowsCount: Optional[int] = Field(alias="windowsCount", default=None,)
	windowsMobileCount: Optional[int] = Field(alias="windowsMobileCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

