from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConfigurationManagerClientEnabledFeatures(BaseModel):
	compliancePolicy: Optional[bool] = Field(default=None,alias="compliancePolicy",)
	deviceConfiguration: Optional[bool] = Field(default=None,alias="deviceConfiguration",)
	inventory: Optional[bool] = Field(default=None,alias="inventory",)
	modernApps: Optional[bool] = Field(default=None,alias="modernApps",)
	resourceAccess: Optional[bool] = Field(default=None,alias="resourceAccess",)
	windowsUpdateForBusiness: Optional[bool] = Field(default=None,alias="windowsUpdateForBusiness",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


