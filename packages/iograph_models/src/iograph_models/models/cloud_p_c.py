from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPC(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	aadDeviceId: Optional[str] = Field(default=None,alias="aadDeviceId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	gracePeriodEndDateTime: Optional[datetime] = Field(default=None,alias="gracePeriodEndDateTime",)
	imageDisplayName: Optional[str] = Field(default=None,alias="imageDisplayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	managedDeviceId: Optional[str] = Field(default=None,alias="managedDeviceId",)
	managedDeviceName: Optional[str] = Field(default=None,alias="managedDeviceName",)
	onPremisesConnectionName: Optional[str] = Field(default=None,alias="onPremisesConnectionName",)
	provisioningPolicyId: Optional[str] = Field(default=None,alias="provisioningPolicyId",)
	provisioningPolicyName: Optional[str] = Field(default=None,alias="provisioningPolicyName",)
	provisioningType: Optional[CloudPcProvisioningType] = Field(default=None,alias="provisioningType",)
	servicePlanId: Optional[str] = Field(default=None,alias="servicePlanId",)
	servicePlanName: Optional[str] = Field(default=None,alias="servicePlanName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .cloud_pc_provisioning_type import CloudPcProvisioningType

