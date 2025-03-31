from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ComanagedDevicesSummary(BaseModel):
	compliancePolicyCount: Optional[int] = Field(alias="compliancePolicyCount", default=None,)
	configurationSettingsCount: Optional[int] = Field(alias="configurationSettingsCount", default=None,)
	endpointProtectionCount: Optional[int] = Field(alias="endpointProtectionCount", default=None,)
	inventoryCount: Optional[int] = Field(alias="inventoryCount", default=None,)
	modernAppsCount: Optional[int] = Field(alias="modernAppsCount", default=None,)
	officeAppsCount: Optional[int] = Field(alias="officeAppsCount", default=None,)
	resourceAccessCount: Optional[int] = Field(alias="resourceAccessCount", default=None,)
	totalComanagedCount: Optional[int] = Field(alias="totalComanagedCount", default=None,)
	windowsUpdateForBusinessCount: Optional[int] = Field(alias="windowsUpdateForBusinessCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

