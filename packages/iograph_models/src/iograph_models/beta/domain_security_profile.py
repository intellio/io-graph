from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DomainSecurityProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activityGroupNames: Optional[list[str]] = Field(alias="activityGroupNames", default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId", default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId", default=None,)
	countHits: Optional[int] = Field(alias="countHits", default=None,)
	countInOrg: Optional[int] = Field(alias="countInOrg", default=None,)
	domainCategories: Optional[list[ReputationCategory]] = Field(alias="domainCategories", default=None,)
	domainRegisteredDateTime: Optional[datetime] = Field(alias="domainRegisteredDateTime", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	registrant: Optional[DomainRegistrant] = Field(alias="registrant", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation", default=None,)

from .reputation_category import ReputationCategory
from .domain_registrant import DomainRegistrant
from .security_vendor_information import SecurityVendorInformation

