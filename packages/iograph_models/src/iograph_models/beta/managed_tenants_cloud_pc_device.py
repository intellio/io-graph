from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsCloudPcDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	cloudPcStatus: Optional[str] = Field(alias="cloudPcStatus", default=None,)
	deviceSpecification: Optional[str] = Field(alias="deviceSpecification", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName", default=None,)
	provisioningPolicyId: Optional[str] = Field(alias="provisioningPolicyId", default=None,)
	servicePlanName: Optional[str] = Field(alias="servicePlanName", default=None,)
	servicePlanType: Optional[str] = Field(alias="servicePlanType", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)


