from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivateLinkDetails(BaseModel):
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	policyName: Optional[str] = Field(alias="policyName",default=None,)
	policyTenantId: Optional[str] = Field(alias="policyTenantId",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


