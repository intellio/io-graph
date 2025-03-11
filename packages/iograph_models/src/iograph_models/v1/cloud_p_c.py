from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPC(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	aadDeviceId: Optional[str] = Field(alias="aadDeviceId",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	gracePeriodEndDateTime: Optional[datetime] = Field(alias="gracePeriodEndDateTime",default=None,)
	imageDisplayName: Optional[str] = Field(alias="imageDisplayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId",default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName",default=None,)
	onPremisesConnectionName: Optional[str] = Field(alias="onPremisesConnectionName",default=None,)
	provisioningPolicyId: Optional[str] = Field(alias="provisioningPolicyId",default=None,)
	provisioningPolicyName: Optional[str] = Field(alias="provisioningPolicyName",default=None,)
	provisioningType: Optional[CloudPcProvisioningType | str] = Field(alias="provisioningType",default=None,)
	servicePlanId: Optional[str] = Field(alias="servicePlanId",default=None,)
	servicePlanName: Optional[str] = Field(alias="servicePlanName",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)

from .cloud_pc_provisioning_type import CloudPcProvisioningType

