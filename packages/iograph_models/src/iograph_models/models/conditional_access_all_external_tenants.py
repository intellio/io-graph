from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessAllExternalTenants(BaseModel):
	membershipKind: Optional[str | ConditionalAccessExternalTenantsMembershipKind] = Field(alias="membershipKind",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

