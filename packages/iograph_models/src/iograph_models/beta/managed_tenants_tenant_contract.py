from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsTenantContract(BaseModel):
	contractType: Optional[int] = Field(alias="contractType", default=None,)
	defaultDomainName: Optional[str] = Field(alias="defaultDomainName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

