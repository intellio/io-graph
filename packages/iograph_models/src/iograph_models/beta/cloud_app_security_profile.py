from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudAppSecurityProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId",default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deploymentPackageUrl: Optional[str] = Field(alias="deploymentPackageUrl",default=None,)
	destinationServiceName: Optional[str] = Field(alias="destinationServiceName",default=None,)
	isSigned: Optional[bool] = Field(alias="isSigned",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	manifest: Optional[str] = Field(alias="manifest",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	permissionsRequired: Optional[ApplicationPermissionsRequired | str] = Field(alias="permissionsRequired",default=None,)
	platform: Optional[str] = Field(alias="platform",default=None,)
	policyName: Optional[str] = Field(alias="policyName",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	riskScore: Optional[str] = Field(alias="riskScore",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation",default=None,)

from .application_permissions_required import ApplicationPermissionsRequired
from .security_vendor_information import SecurityVendorInformation

