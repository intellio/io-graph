from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerClientEnabledFeatures(BaseModel):
	compliancePolicy: Optional[bool] = Field(alias="compliancePolicy",default=None,)
	deviceConfiguration: Optional[bool] = Field(alias="deviceConfiguration",default=None,)
	endpointProtection: Optional[bool] = Field(alias="endpointProtection",default=None,)
	inventory: Optional[bool] = Field(alias="inventory",default=None,)
	modernApps: Optional[bool] = Field(alias="modernApps",default=None,)
	officeApps: Optional[bool] = Field(alias="officeApps",default=None,)
	resourceAccess: Optional[bool] = Field(alias="resourceAccess",default=None,)
	windowsUpdateForBusiness: Optional[bool] = Field(alias="windowsUpdateForBusiness",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


