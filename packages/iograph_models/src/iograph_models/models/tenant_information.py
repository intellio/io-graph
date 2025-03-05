from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TenantInformation(BaseModel):
	defaultDomainName: Optional[str] = Field(default=None,alias="defaultDomainName",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	federationBrandName: Optional[str] = Field(default=None,alias="federationBrandName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


