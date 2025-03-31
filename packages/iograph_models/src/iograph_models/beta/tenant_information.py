from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TenantInformation(BaseModel):
	defaultDomainName: Optional[str] = Field(alias="defaultDomainName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	federationBrandName: Optional[str] = Field(alias="federationBrandName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

