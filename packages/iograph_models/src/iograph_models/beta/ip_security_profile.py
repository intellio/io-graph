from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IpSecurityProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activityGroupNames: Optional[list[str]] = Field(alias="activityGroupNames",default=None,)
	address: Optional[str] = Field(alias="address",default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId",default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId",default=None,)
	countHits: Optional[int] = Field(alias="countHits",default=None,)
	countHosts: Optional[int] = Field(alias="countHosts",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	ipCategories: Optional[list[IpCategory]] = Field(alias="ipCategories",default=None,)
	ipReferenceData: Optional[list[IpReferenceData]] = Field(alias="ipReferenceData",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	riskScore: Optional[str] = Field(alias="riskScore",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation",default=None,)

from .ip_category import IpCategory
from .ip_reference_data import IpReferenceData
from .security_vendor_information import SecurityVendorInformation

