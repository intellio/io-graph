from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessCrossTenantSummary(BaseModel):
	authTransactionCount: Optional[int] = Field(alias="authTransactionCount",default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)
	newTenantCount: Optional[int] = Field(alias="newTenantCount",default=None,)
	rarelyUsedTenantCount: Optional[int] = Field(alias="rarelyUsedTenantCount",default=None,)
	tenantCount: Optional[int] = Field(alias="tenantCount",default=None,)
	userCount: Optional[int] = Field(alias="userCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


