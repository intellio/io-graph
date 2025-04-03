from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedTenantsTenantDetailedInformation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.tenantDetailedInformation"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.tenantDetailedInformation")
	city: Optional[str] = Field(alias="city", default=None,)
	countryCode: Optional[str] = Field(alias="countryCode", default=None,)
	countryName: Optional[str] = Field(alias="countryName", default=None,)
	defaultDomainName: Optional[str] = Field(alias="defaultDomainName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	industryName: Optional[str] = Field(alias="industryName", default=None,)
	region: Optional[str] = Field(alias="region", default=None,)
	segmentName: Optional[str] = Field(alias="segmentName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	verticalName: Optional[str] = Field(alias="verticalName", default=None,)

